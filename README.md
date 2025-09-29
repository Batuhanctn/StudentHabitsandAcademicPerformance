# Student Habits and Academic Performance Prediction 🎓

A machine learning web application that predicts student academic performance based on their lifestyle habits and behaviors.

## 📋 Project Overview

This project analyzes the relationship between student habits and academic performance using machine learning algorithms. The application provides a user-friendly web interface where students can input their lifestyle data and receive academic performance predictions.

## 🚀 Features

- **Interactive Web Interface**: Modern, responsive design with intuitive form inputs
- **Real-time Predictions**: Instant academic performance scoring based on 14 lifestyle parameters
- **Data Validation**: Comprehensive input validation and error handling
- **Performance Categories**: Results categorized from "Excellent" to "Needs Improvement"
- **Mobile Responsive**: Works seamlessly across desktop and mobile devices

## 📊 Input Parameters

The model analyzes the following student characteristics:

### Demographics
- Age (16-30)
- Gender

### Study Habits
- Daily study hours
- Class attendance percentage

### Digital Lifestyle
- Daily social media usage
- Netflix/streaming hours

### Health & Lifestyle
- Sleep hours per night
- Exercise frequency (days per week)
- Diet quality
- Mental health rating (1-10)

### Work & Activities
- Part-time job status
- Extracurricular participation

### Family & Environment
- Parental education level
- Internet connection quality

## 🛠️ Technologies Used

### Backend
- **Python 3.x**
- **FastAPI** - Modern web framework for building APIs
- **Pandas** - Data manipulation and analysis
- **Scikit-learn** - Machine learning algorithms
- **Pickle** - Model serialization

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with gradients and animations
- **JavaScript (ES6+)** - Interactive functionality and API calls

### Data Processing
- **Label Encoders** - Categorical variable encoding
- **Ordinal Encoders** - Ordered categorical features
- **Feature Engineering** - Data preprocessing and transformation

## 📁 Project Structure

```
StudentHabitsProject/
│
├── app.py                 # FastAPI backend application
├── requirements.txt       # Python dependencies
├── final_project.pkl     # Trained ML model and encoders
├── model_test.py         # Model testing script
├── testdata.csv          # Sample test data
│
└── templates/
    └── index.html        # Frontend web interface
```

## ⚡ Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/Batuhanctn/StudentHabitsandAcademicPerformance.git
cd StudentHabitsandAcademicPerformance
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
uvicorn app:app --reload
```

4. **Open your browser**
Navigate to `http://localhost:8000`

## 🎯 How to Use

1. Fill out the form with your personal information and habits
2. Click "Predict My Academic Performance"
3. View your predicted academic performance score
4. Get personalized recommendations based on your results

## 📈 Model Performance

The machine learning model uses various algorithms to predict academic performance with high accuracy. The model was trained on a comprehensive dataset from Kaggle containing student lifestyle and academic data.

## 🎨 UI Features

- **Glassmorphism Design**: Modern transparent card design
- **Smooth Animations**: Hover effects and loading states
- **Color-coded Results**: Visual feedback with emojis and colors
- **Form Validation**: Real-time input validation
- **Responsive Layout**: Mobile-first design approach

## 🔧 API Endpoints

### GET /
Returns the main web interface

### POST /predict
Accepts student data and returns academic performance prediction

**Request Body:**
```json
{
  "age": 20,
  "gender": "Male",
  "study_hours_per_day": 4.5,
  "social_media_hours": 2.0,
  "netflix_hours": 1.5,
  "part_time_job": "No",
  "attendance_percentage": 85.0,
  "sleep_hours": 7.0,
  "diet_quality": "Good",
  "exercise_frequency": 3,
  "parental_education_level": "Bachelor",
  "internet_quality": "Good",
  "mental_health_rating": 8,
  "extracurricular_participation": "Yes"
}
```

**Response:**
```json
{
  "prediction": 78.5
}
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Batuhan Cetin**
- GitHub: [@Batuhanctn](https://github.com/Batuhanctn)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/batuhan-çetin-963155266/)

## 🙏 Acknowledgments

- Dataset from Kaggle: "Student Habits vs Academic Performance"
- Course: "Veri Bilimi ve Makine Öğrenmesi 2025: 100 Günlük Kamp" by Atıl Samancıoğlu
- FastAPI documentation and community

## 📊 Future Improvements

- [ ] Add more sophisticated ML models (Neural Networks, Ensemble methods)
- [ ] Implement data visualization dashboard
- [ ] Add user authentication and data persistence
- [ ] Create mobile app version
- [ ] Add A/B testing for UI improvements
- [ ] Implement model retraining capabilities

---

⭐ **Star this repository if you found it helpful!**
