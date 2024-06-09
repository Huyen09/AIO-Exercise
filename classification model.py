#funtion caculate 
def F1core(tp,fp,fn):
  P = tp/(tp+fp)
  R = tp/(tp+fn)
  F1 = 2*((P*R)/(P+R))
  return F1,P,R
try:
  # nhập các giá trị tp,fp,fn
  tp = int(input("Nhập giá trị tp: "))
  fp = int(input("Nhập giá trị tp: "))
  fn = int(input("Nhập giá trị tp: "))
  # kiểm tra giá trị nhập có lớn 0
  if tp <= 0 or fp <= 0 or fn <= 0:
    print("gia tri phai lon hon 0")
  else:
    # trả các giá trị nhập vào ham·
    F1, P, R = F1core(tp, fp, fn)
    print(f"P = {P:.4f}")
    print(f"R = {R:.4f}")
    print(f"F1 = {F1:.4f}")
except ValueError:
  print("gia tri phai la int")

  