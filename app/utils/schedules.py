from flask_apscheduler import APScheduler
# from app.controllers import lost_messages

scheduler = APScheduler()


@scheduler.task('interval', id='do_job_1', minutes=60)
def verify_lost_messages():
    """
    Para cambiar el intervalo a segundos usar la palabra seconds en el decorador.

    :return: {void}
    """

    print("---- verify_lost_messages() ejecutado")
    # lost_messages.restore_messages()
