import turtle as t
import datetime as d
def skip(step):
  t.penup()
  t.forward(step)
  t.pendown()
def drawClock(radius):
  t.speed(0)
  t.mode("logo")
  t.hideturtle()
  t.pensize(7)
  t.home()
  for j in range(60):
    skip(radius)
    if (j % 5 == 0):
      t.forward(20)
      skip(-radius - 20)
    else:
      t.dot(5)
      skip(-radius)
    t.right(6)
def makePoint(pointName, len):
  t.penup()
  t.home()
  t.begin_poly()
  t.back(0.1 * len)
  t.forward(len * 1.1)
  t.end_poly()
  poly = t.get_poly()
  t.register_shape(pointName, poly)
def drawPoint():
  global hourPoint, minPoint, secPoint, fontWriter
  makePoint("hourPoint",100)
  makePoint("minPoint",120)
  makePoint("secPoint",140)
  hourPoint = t.Pen()
  hourPoint.shape("hourPoint")
  hourPoint.shapesize(1,1,6)
  minPoint = t.Pen()
  minPoint.shape("minPoint")
  minPoint.shapesize(1,1,4)
  secPoint = t.Pen()
  secPoint.shape("secPoint")
  secPoint.pencolor('red')
  fontWriter = t.Pen()
  fontWriter.pencolor('gray')
  fontWriter.hideturtle()
def getWeekName(weekday):
  weekName = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
  return weekName[weekday]
def getDate(year,month,day):
  return "%s-%s-%s" % (year,month,day)
def realTime():
  curr = d.datetime.now()
  curr_year = curr.year
  curr_month = curr.month
  curr_day = curr.day
  curr_hour = curr.hour
  curr_minute = curr.minute
  curr_second = curr.second
  curr_weekday = curr.weekday()
  t.tracer(False)
  secPoint.setheading(360 / 60 * curr_second)
  minPoint.setheading(360 / 60 * curr_minute)
  hourPoint.setheading(360 / 12 * curr_hour + 30 / 60 * curr_minute)
  fontWriter.clear()
  fontWriter.home()
  fontWriter.penup()
  fontWriter.forward(80)
  fontWriter.write(getWeekName(curr_weekday), align="center",font=("Courrier",14,"bold"))
  fontWriter.forward(-160)
  fontWriter.write(getDate(curr_year, curr_month, curr_day), align="center",font=("Courrier",14,"bold"))
  t.tracer(True)
  t.ontimer(realTime,100)
def main():
  t.tracer(False)
  drawClock(160)
  drawPoint()
  realTime()
  t.tracer(True)
  t.mainloop()
if __name__ == '__main__':
  main()
