import psycopg2
from datetime import datetime, timedelta

def connect_to_database():
    try:
        
        user = input("Nhập tên user: ")
        password = input("Nhập mật khẩu: ")
        host = input("Nhập địa chỉ host: ")
        port = input("Nhập số cổng: ")
        database = input("Nhập tên cơ sở dữ liệu: ")

        
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        return connection

    except Exception as e:
        print(f"Lỗi khi kết nối đến database: {e}")
        return None

def delete_data(connection, table_name, time_column, start_time, end_time):
    try:
    
        cursor = connection.cursor()

        if time_column:
            delete_query = f"DELETE FROM {table_name} WHERE {time_column} >= %s AND {time_column} <= %s"
            cursor.execute(delete_query, (start_time, end_time))
        else:
            delete_query = f"DELETE FROM {table_name}"
            cursor.execute(delete_query)

        
        connection.commit()
        cursor.close()

        print("Dữ liệu đã được xóa thành công!")

    except Exception as e:
        print(f"Lỗi khi xóa dữ liệu: {e}")

def main():
    connection = connect_to_database()

    if connection:
        try:
            table_name = input("Nhập tên bảng: ")
            time_column = input("Nhập tên cột thời gian (để trống nếu không có): ")

            start_time_str = input("Nhập thời gian bắt đầu (YYYY-MM-DD HH:MM:SS): ")
            end_time_str = input("Nhập thời gian kết thúc (YYYY-MM-DD HH:MM:SS): ")

            start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")

            delete_data(connection, table_name, time_column, start_time, end_time)

        finally:
    
            connection.close()

if __name__ == "__main__":
    main()
