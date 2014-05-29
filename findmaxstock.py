#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys


class CSVStock():
  """  
  this will load csv file into memory read each row of stock data of companies.
  """
  def __init__(self,csv_file):
    self.read_file_content(csv_file)
    self.results = {}

  def read_file_content(self,csv_file):
    """  
    open csv file if its not readable or not able to open will raise I/O exception.
    using csv reader get content of file and set columns that is header(first row of file)
    """
    try:
      self.csv_file = open(csv_file,'r')
      self.csv_content = csv.reader(self.csv_file)
      self.columns = self.csv_content.next()
    except IOError:
      print "Not able to open file...."

  def set_max_stock(self):
    """  
    find and set max stocks corrosponding to the company, 
    if these max stocks are same accros the multiple year-month then append into list for the same comapany
    """
    if self.csv_content:
      try:
        for row in self.csv_content:
          for index, column in enumerate(self.columns):
            if index >1:
              if not self.results.get(column):
                self.results[column] = [tuple([row[index], row[0], row[1]])]
              else:
                if float(row[index]) > float(self.results[column][0][0]):
                  self.results[column] = [tuple([row[index], row[0], row[1]])]
                elif float(row[index]) == float(self.results[column][0][0]):
                  self.results[column].append(tuple([row[index], row[0], row[1]]))

      except Exception:
        self.results = None
        print "csv doesn't have valid data...."
        return False
    return True

  def get_max_stock(self):
    """  
    get a result list of dict of all max stocks for multiple companies, taht has been set using set_max_stock 
    """
    return self.results

  def close_file(self):
    """  
    close open csv file
    """
    if self.csv_file:
      self.csv_file.close() 
    
  def print_stocks(self):
    """  
    print results as an end user readable format
    """
    if self.results:
      print "*"*50
      print "%s %s %s %s " %("COMPANY".ljust(20), "PRICE".ljust(10), "YEAR".ljust(10), "MONTH".ljust(10))
      temp_comp = ""
      for company, tpl in self.results.iteritems():
        for item in tpl:
          if temp_comp == company:
            company = ""
          print "%s %s %s %s %s" %(" ",company.ljust(18),item[0].ljust(10),item[1].ljust(10),item[2].ljust(10))
          temp_comp = company

      print "*"*50
   
if __name__ == '__main__':
  """  
  start from here, just taking inputa as a csv file and validation if its not contained valid data or invalid format etc.. 
  if it is ok proceed with reading and find max stock with CSVStock object
  """
  if len(sys.argv)>=2:
    csv_file = sys.argv[1]
    if not csv_file.endswith('.csv'):    
      print "Not a vaid csv file..."
    else:
      try:
        csv_stock = CSVStock(csv_file)
        csv_stock.set_max_stock()
        csv_stock.print_stocks()
        csv_stock.close_file()
      except Exception:
        print "Please Input valid csv file...."

  else:
    print "No Input file..."


