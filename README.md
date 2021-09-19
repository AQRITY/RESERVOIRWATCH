# WAVE2WEB HACKATHON - RESERVOIRWATCH DASHBOARD 
## AQRITY

### Welcome to our repository for the WAVE2WEB Hackathon

Our interactive dashboard helps in dissemination of information regarding near-real time prediction of water availability in four dams of the Upper Cauvery river basin that supply water to Bangalore City. We have adopted a physically described process-based approach that lends information to a machine learning model to come about with a 30, 60 and 90 day prediction of storage capacity and inflows. Prediction of water storage and inflow to a reservoir helps in deciding outflows from the dam to fulfil different water demands. This will be useful for the public and various stakeholders in making scientifically informed decisions.

### The repository has been structured based on
- python scripts used to extract data from satellite and reanalysis data
- outputs of the Hydrological Model
- outputs of the AI/ML Models for storage and inflow
- dashboard frontend

### Hydrological Model

- SWAT (Soil and Water Assesment Tool), a semi-distributed model has been used to understand the physical processes at play upstream of the four dams (Hemavathi, Harangi, Kabini and KRS)
- The model folder and files can be accessed [here](https://drive.google.com/drive/folders/1Z8Cff8hQNjiEutE76atbjrNk2J5_oQoz)
- For more details on hydrological modeling, refer to the technical documentation

### AI/ML Model

- Three different model architectures were explored : Fully Connected Dense Neural Networks, Recurrent Neural Networks and WaveNets. 
- After much experimentation, we decided on Recurrent Neural Networks - specifically the Long-Short Term Memory architecture.
- Monte-Carlo Ensemble Model has been adopted to convert our single deterministic predictions into probability distribution functions to find an uncertainty estimate.
- For more details on our AI/ML model, refer to the technical documentation.

### Interactive Dashboard

- The dashboard has two views - overview and dataview.
- Time-series data related to historical and future predictions are shown.
- Model comparison of predictions vs observed has been done for the year Jan 2020 to Dec 2020

The RESERVOIRWATCH Dashboard can be accessed at [www.aqrity.com/reservoirwatch](http://reservoir-watch.aqrity.com/)