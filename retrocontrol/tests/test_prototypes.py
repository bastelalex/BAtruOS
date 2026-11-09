import csv
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('placement', ROOT/'mechanical/placement.py')
placement = importlib.util.module_from_spec(spec)
spec.loader.exec_module(placement)
class Prototypes(unittest.TestCase):
    def test_demo_formats(self):
        with tempfile.TemporaryDirectory() as d:
            exe = str(Path(d)/'sim')
            subprocess.run(['g++','-std=c++17','-Wall','-Wextra','-Werror',str(ROOT/'firmware/sim.cpp'),'-o',exe],check=True)
            lines = subprocess.check_output([exe],text=True).splitlines()
        self.assertEqual(len(lines),33)
        previous = -1
        for i in range(1,len(lines),2):
            row = next(csv.DictReader(io.StringIO(lines[0]+'\n'+lines[i])))
            frame = json.loads(lines[i+1])
            for key,value in frame.items(): self.assertEqual(row[key],str(value))
            self.assertEqual(frame['source'],'synthetic')
            self.assertEqual(frame['quality'],'demo')
            self.assertEqual(frame['state'],'DEMO')
            self.assertGreater(frame['timestamp_ms'],previous)
            self.assertIn(frame['channel'],range(8))
            previous=frame['timestamp_ms']
    def test_example(self):
        with tempfile.TemporaryDirectory() as d:
            target=Path(d)/'placement.scad'
            placement.convert(ROOT/'mechanical/placement.example.csv',target)
            self.assertIn('[[20.0, 20.0, 0.0], [60.0, 40.0, 90.0]]',target.read_text())
    def test_invalid(self):
        cases=['','R1,nan,0,0,top\n','R1,101,0,0,top\n','R1,0,-1,0,top\n','R1,0,0,0,bottom\n','R1,0,0,0,top\nR1,1,1,0,top\n','R1,0,0,inf,top\n']
        with tempfile.TemporaryDirectory() as d:
            source,target=Path(d)/'in.csv',Path(d)/'out.scad'
            for body in cases:
                with self.subTest(body=body):
                    source.write_text('reference,x_mm,y_mm,rotation_deg,side\n'+body)
                    with self.assertRaises(ValueError): placement.convert(source,target)
