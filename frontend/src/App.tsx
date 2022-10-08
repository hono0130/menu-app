import React, { FC } from 'react'
import NavBar from './component/Header'
import './App.css'

import Logo from './component/Logo'
import DishTable from './component/DishTable'

const App: FC = () => {
  return (
    <div className="App">
      <NavBar />
      <h1>不要な料理を選んでください</h1>
      <DishTable
        rows={[
          {
            id: 0,
            dishes: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/10/negidare-karaage-400x267.jpg',
                name: 'ねぎだれ鶏唐揚げ',
                duration: 20,
                tag: '鶏肉',
              },
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2019/05/chicken-steak-garlcic-shoyu.jpg',
                name: 'ガーリック醤油チキンステーキ',
                duration: 15,
                tag: '鶏肉',
              },
            ],
          },
          {
            id: 1,
            dishes: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/10/negidare-karaage-400x267.jpg',
                name: 'ねぎだれ鶏唐揚げ',
                duration: 20,
                tag: '鶏肉',
              },
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2019/05/chicken-steak-garlcic-shoyu.jpg',
                name: 'ガーリック醤油チキンステーキ',
                duration: 15,
                tag: '鶏肉',
              },
            ],
          },
          {
            id: 2,
            dishes: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/10/negidare-karaage-400x267.jpg',
                name: 'ねぎだれ鶏唐揚げ',
                duration: 20,
                tag: '鶏肉',
              },
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2019/05/chicken-steak-garlcic-shoyu.jpg',
                name: 'ガーリック醤油チキンステーキ',
                duration: 15,
                tag: '鶏肉',
              },
            ],
          },
        ]}
      ></DishTable>
    </div>
  )
}

export default App
