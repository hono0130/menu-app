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
            id: 1,
            Lunch: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/10/negidare-karaage-400x267.jpg',
                name: 'ねぎだれ鶏唐揚げ',
                duration: 20,
                tag: '鶏肉',
                isSideDish: false,
              },
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/05/chuka-harusame-salad-400x267.jpg',
                name: '中華春雨サラダ',
                duration: 10,
                tag: '春雨',
                isSideDish: true,
              },
            ],
            Dinner: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2019/05/chicken-steak-garlcic-shoyu.jpg',
                name: 'ガーリック醤油チキンステーキ',
                duration: 15,
                tag: '鶏肉',
                isSideDish: true,
              },
              {
                imageURL: 'https://cookien.com/wp-content/uploads/2019/02/iri-dofu.jpg',
                name: '炒り豆腐',
                duration: 10,
                tag: '豆腐',
                isSideDish: true,
              },
            ],
          },
          {
            id: 2,
            Lunch: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/10/negidare-karaage-400x267.jpg',
                name: 'ねぎだれ鶏唐揚げ',
                duration: 20,
                tag: '鶏肉',
                isSideDish: false,
              },
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2019/05/chicken-steak-garlcic-shoyu.jpg',
                name: 'ガーリック醤油チキンステーキ',
                duration: 15,
                tag: '鶏肉',
                isSideDish: true,
              },
            ],
            Dinner: [
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2022/10/negidare-karaage-400x267.jpg',
                name: 'ねぎだれ鶏唐揚げ',
                duration: 20,
                tag: '鶏肉',
                isSideDish: false,
              },
              {
                imageURL:
                  'https://cookien.com/wp-content/uploads/2019/05/chicken-steak-garlcic-shoyu.jpg',
                name: 'ガーリック醤油チキンステーキ',
                duration: 15,
                tag: '鶏肉',
                isSideDish: true,
              },
            ],
          },
        ]}
      ></DishTable>
    </div>
  )
}

export default App
