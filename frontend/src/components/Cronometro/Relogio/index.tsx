import style from './Relogio.module.scss';

interface Props {
    tempo: number | undefined
}

export default function Relogio({tempo = 0}:Props) {

    const minutos = String(Math.floor(tempo / 60)).padStart(2, '0');
    const segundos = String(tempo % 60).padStart(2, '0');

    return (
        <>
            <span className={style.relogioNumero}>{minutos[0]}</span>
            <span className={style.relogioNumero}>{minutos[1]}</span>
            <span className={style.relogioDivisao}>:</span>
            <span className={style.relogioNumero}>{segundos[0]}</span>
            <span className={style.relogioNumero}>{segundos[1]}</span>
        </>
    )
}