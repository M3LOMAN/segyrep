FROM miheevdocker/whobs

WORKDIR /C:/Users/Владимир/OneDrive/Документы/makeSGY

COPY . .

ENTRYPOINT ["python3"]

CMD ["sgypy.py"]