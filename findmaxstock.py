#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys


class CSVStock():
  def __init__(self,csv_file):
    self.read_file_content(csv_file)
    self.results = {}

  def read_file_content(self,csv_file):
    try:
      self.csv_file = open(csv_file,'r')
      self.csv_content = csv.reader(self.csv_file)
      self.columns = self.csv_content.next()
    except IOError:
      print "Not able to open file...."

  def get_results(self):
    return self.results
    
  def find_max(self):
    if self.csv_content:
      try:
        for row in self.csv_content:
          for index, column in enumerate(self.columns):
            if index >1:
              if self.results.get(column):
                if float(row[index]) > self.results.get(column).get('price'):
                  self.results[column]['price'] = float(row[index])
                  self.results[column]['year_month'] = ["%s, %s" %(row[0], row[1])]
                elif float(row[index]) == self.results.get(column).get('price'):
                  self.results[column]['year_month'].append("%s, %s" %(row[0], row[1]))
              elif not self.results.get(column):
                  self.results[column] = {'price':float(row[index]), 'year_month':["%s, %s" %(row[0], row[1])]}
      except Exception:
        self.results = None
        print "csv doesn't have valid data...."
        return False
    return True
   
if __name__ == '__main__':
  if len(sys.argv)>=2:
    csv_file = sys.argv[1]
    if not csv_file.endswith('.csv'):    
      print "Not a vaid csv file..."
    else:
      try:
        csv_stock = CSVStock(csv_file)
        csv_stock.find_max()
        results  = csv_stock.get_results()
        if results:
          for key, value in results.iteritems():
            print "%s => %s" %(key, value)
      except Exception:
        print "Please Input valid csv file...."

  else:
    print "No Input file..."


