"""

    Dictionary which contains title and abstracts 

"""

sample_data={
            'Mobile Search Behaviors: An In-depth Analysis Based on Contexts, APPs, and Devices':'With the rapid development of mobile Internet and smart personal devices in recent years, mobile search has gradually emerged as a key method with which users seek online information. In addition, cross-device search also has been regarded recently as an important research topic. As more mobile applications (APPs) integrate search functions, a user"s mobile search behavior on different APPs becomes more significant. This book provides a systematic review of current mobile search analysis and studies user mobile search behavior from several perspectives, including mobile search context, APP usage, and different devices. Two different user experiments to collect user behavior data were conducted. Then, through the data from user mobile phone usage logs in natural settings, we analyze the mobile search strategies employed and offer a context-based mobile search task collection, which then can be used to evaluate the mobile search engine. In addition, we combine mobile search with APP usage to give more in-depth analysis, such as APP transition in mobile search and follow-up actions triggered by mobile search. The study, combining the mobile search with APP usage, can contribute to the interaction design of APPs, such as the search recommendation and APP recommendation. Addressing the phenomenon of users owning more smart devices today than ever before, we focus on user cross device search behavior. We model the information preparation behavior and information resumption behavior in cross-device search and evaluate the search performance in cross-device search. Research on mobile search behaviors across different devices can help to understand online user information behavior comprehensively and help users resume their search tasks on different devices',#1
            'A Sequential Recommendation for Mobile Apps: What will User Click Next App?':'With the advances in smartphones users install abundant apps to facilitate their daily lives. Both users and related developers have increasing requirements to understand the mobile App usage pattern, for individual and commercial use. Respectively, personalized App recommendation methods and systems have emerged as a novel attractive topic that can demonstrate the human App usage behavior. The mobile Apps recommendation can serve as a cornerstone for a variety of intelligent services, such as fast-launching UIs, intelligent user phone interactions, and battery management of cellphones. In this paper, we develop a novel App recommendation framework combining the historical App usage data with the sequence of recently-used Apps. Speciﬁcally, our framework is an extension of the user-based collaborative ﬁltering technique, where the set of nearest neighbors is employed for training the prediction model. However, our prediction scheme is constructed on the temporal sequential data and is modeled by using the chain augmented Naive Bayes model. Experiments with a real mobile Internet record dataset demonstrate that the accuracy of our framework outperforms several baseline App recommendation approaches.',#2
            'Helicopter Navigation in Coastal Zone  Based on Terrestrial Radio-Beacon System':'In certain scenarios, especially in areas of armed conflict, the use of satellite navigation may be inaccurate or impossible. In such cases, it is desirable to use backup terrestrial navigation systems. In 2016, we proposed the concept of such a system dedicated to vessels. Its basis is a radio-beacon system deployed on lighthouses along the coast. The proposed medium-range navigation system for use in the coastal zone is based on the signal Doppler frequency (SDF) method. In this paper, we analyze the possibility of positioning a helicopter based on this system. This assessment is based on simulation studies.',#3
            'Optimization of cost to calculate the release time in software reliability using python':'As the competition among softwares have been increasing day by day, it made the IT sector to grow at different level. Whenever a software product comes into the market, a list of factors begin to originate and demand for changes. Hence there can arise defects in the software and so defects needed to be repaired. Also sales and demands of softwares are  increasing day by day . So it becomes difficult to decide which software will be appropriate for the customer. As competitors are adding features and functions everyday to evolve technology that requires new upgrades to support latest versions of software. In order to maintain these new features, to win over prospects , testing is required to be done. Testing can be seen for technical case, business case, and economical case and especially for the reliability estimation.The prediction of faults in the software is another term in case of determining the outcome of the software product and the certain number of testing will be needed. Software reliability models techniques are employed for the perfect optimization on its release time. This research gives the idea of using both original release time and predicted release time to be executed and hence to obtain an optimized cost for  release time. This will help to decide the effective cost of reliability of the software. Further going, this will help the customer to have the better selection on choosing the effective software. Thus through the python we have optimized the cost and found the release time of software to decide that this software will give the better output.',#4
            'The Collaborative Virtual Reality Neurorobotics Lab':'We present the collaborative Virtual Reality Neurorobotics Lab, which allows multiple collocated and remote users to experience, discuss and participate in neurorobotic experiments in immersive virtual reality. We describe the coupling of the Neurorobotics Platform of the Human Brain Project with our collaborative virtual reality and 3D telepresence infrastructure and highlight future opportunities arising from our work for research on direct human interaction with simulated robots and brains.',#5
            'Block Design-Based Key Agreement for Group Data Sharing in Cloud Computing':'Data sharing in cloud computing enables multiple participants to freely share the group data, which improves the efficiency of work in cooperative environments and has widespread potential applications. However, how to ensure the security of data sharing within a group and how to efficiently share the outsourced data in a group manner are formidable challenges. Note that key agreement protocols have played a very important role in secure and efficient group data sharing in cloud computing. In this paper, by taking advantage of the symmetric balanced incomplete block design (SBIBD), we present a novel block design-based key agreement protocol that supports multiple participants, which can flexibly extend the number of participants in a cloud environment according to the structure of the block design. Based on the proposed group data sharing model, we present general formulas for generating the common conference key IC for multiple participants. Note that by benefiting from the (v, k + 1, 1)-block design, the computational complexity of the proposed protocol linearly increases with the number of participants and the communication complexity is greatly reduced. In addition, the fault tolerance property of our protocol enables the group data sharing in cloud computing to withstand different key attacks, which is similar to Yi"s protocol.',#6
            'One Quantifiable Security Evaluation Model for Cloud Computing Platform':'Whatever one public cloud, private cloud or a mixed cloud, the users lack of effective security quantifiable evaluation methods to grasp the security situation of its own information infrastructure on the whole. This paper provides a quantifiable security evaluation system for different clouds that can be accessed by consistent API. The evaluation system includes security scanning engine, security recovery engine, security quantifiable evaluation model, visual display module and etc. The security evaluation model composes of a set of evaluation elements corresponding different fields, such as computing, storage, network, maintenance, application security and etc. Each element is assigned a three tuple on vulnerabilities, score and repair method. The system adopts “One vote vetoed” mechanism for one field to count its score and adds up the summary as the total score, and to create one security view. We implement the quantifiable evaluation for different cloud users based on our G-Cloud platform. It shows the dynamic security scanning score for one or multiple clouds with visual graphs and guided users to modify configuration, improve operation and repair vulnerabilities, so as to improve the security of their cloud resources.',#7            
            'Brain inspired cognitive artificial intelligence for knowledge extraction and intelligent instrumentation system':'Artificial intelligence evolves with the development of computers even rely on computational development. The ways and processes of human thinking developed by Psychologists and welcomed by computational experts produce the science of Artificial Intelligence. This continues with the development of cognitive science that encourages the development of Artificial Intelligence to Cognitive Thinking Intelligence, a new pathway to the science of Artificial Intelligence that can emulate human cognitive abilities even if not 100%. Emulation of human cognitive abilities is developed based on the modeling of system interaction with the environment and information fusion, which can be used to conduct Inferencing, so when this occurs repeatedly it will produce knowledge that grows. This process is called Knowledge Growing System which is Brain Inspired Cognitive Artificial Intelligence and can be used for information extraction and when applied to instrumentation system will realize Intelligent Instrumentation System.', # 1
            'Amplifying the Social Intelligence of Teams Through Human Swarming':'Artificial Swarm Intelligence (ASI) is a method for amplifying the collective intelligence of human groups by connecting networked participants into real-time systems modeled after natural swarms and moderated by AI algorithms. ASI has been shown to amplify performance in a wide range of tasks, from forecasting financial markets to prioritizing conflicting objectives. This study explores the ability of ASI systems to amplify the social intelligence of small teams. A set of 61 teams, each of 3 to 6 members, was administered a standard social sensitivity test -“Reading the Mind in the Eyes” or RME. Subjects took the test both as individuals and as ASI systems (i.e. “swarms”). The average individual scored 24 of 35 correct (32% error) on the RME test, while the average ASI swarm scored 30 of 35 correct (15% error). Statistical analysis found that the groups working as ASI swarms had significantly higher social sensitivity than individuals working alone or groups working together by plurality vote (p<;0.001). This suggests that when groups reach decisions as real-time ASI swarms, they make better use of their social intelligence than when working alone or by traditional group vote.', # 2
            'One Quantifiable Security Evaluation Model for Cloud Computing Platform':'Whatever one public cloud, private cloud or a mixed cloud, the users lack of effective security quantifiable evaluation methods to grasp the security situation of its own information infrastructure on the whole. This paper provides a quantifiable security evaluation system for different clouds that can be accessed by consistent API. The evaluation system includes security scanning engine, security recovery engine, security quantifiable evaluation model, visual display module and etc. The security evaluation model composes of a set of evaluation elements corresponding different fields, such as computing, storage, network, maintenance, application security and etc. Each element is assigned a three tuple on vulnerabilities, score and repair method. The system adopts “One vote vetoed” mechanism for one field to count its score and adds up the summary as the total score, and to create one security view. We implement the quantifiable evaluation for different cloud users based on our G-Cloud platform. It shows the dynamic security scanning score for one or multiple clouds with visual graphs and guided users to modify configuration, improve operation and repair vulnerabilities, so as to improve the security of their cloud resources.', # 3
            'Connecting Fog and Cloud Computing':'There is a perfect storm of the use of cloud computing, and the growth of Internet of Things (IoT). IoT is about processing data that comes from devices in some way that is meaningful, and cloud computing is about leveraging data from centralized computing and storage. Growth rates of both can easily become unmanageable. We have some problems to solve. In addition, alternatives are being consider to placing everything in the public cloud because the public cloud, in some cases, no longer makes sense.', # 4
            'Big Data Quality Framework: Pre-Processing Data in Weather Monitoring Application':"Big Data has become an imminent part of all industries and business sectors today. All organizations in any sector like energy, banking, retail, hardware, networking, etc all generate huge quantum of heterogenous data which if mined, processed and analyzed accurately can reveal immensely useful patterns for business heads to apply to generate and grow their businesses. Big Data helps in acquiring, processing and analyzing large amounts of heterogeneous data to derive valuable results. Quality of information is affected by size, speed and format in which data is generated. Hence, Quality of Big Data is of great relevance and importance. We propose addressing various aspects of the raw data to improve its quality in the pre-processing stage, as the raw data may not usable as-is. We are exploring process like Cleansing to fix as much data as feasible, Noise filters to remove bad data, as well sub-processes for Integration and Filtering along with Data Transformation/Normalization. We evaluate and profile the Big Data during acquisition stage, which is adapted to expectations to avoid cost overheads later while also improving and leading to accurate data analysis. Hence, it is imperative to improve Data quality even it is absorbed and utilized in an industry's Big Data system. In this paper, we propose a Pre-Processing Framework to address quality of data in a weather monitoring and forecasting application that also takes into account global warming parameters and raises alerts/notifications to warn users and scientists in advance.", # 5
            'An OWL Ontology for Supporting Semantic Services in Big Data Platforms':"In the last years, there was a growing interest in the use of Big Data models to support advanced data analysis functionalities. Many companies and organizations lack IT expertise and adequate budget to have benefits from them. In order to fill this gap, a model-based approach for Big Data Analytics-as-a-service (MBDAaaS) can be used. The proposed model, composed by declarative, procedural and deployment (sub) models, can be used to select a deployable set of services based on a set of user preferences shaping a Big Data Campaign (BDC). The deployment of a BDC requires that the selection of services has to be carried out on the basis of coherent and non conflictual user preferences. In this paper we propose an OWL ontology in order to solve this issue.", # 6
            'Effective Scheme against 51% Attack on Proof-of-Work Blockchain with History Weighted Information':"Proof-of-Work (PoW) is a popular protocol used in Blockchain systems to resolve double-spending problems. However, if an attacker has access to calculation hash power greater than half of the total hash power, this attacker can create a double-spending attack or 51% attack. The cost of creating a 51% attack is surprisingly low if hash power is abundantly available. That posts a great threat to lots of PoW blockchains. We propose a technique to combine history weighted information of miners with the total calculation difficulty to alleviate the 51% attack problem. Analysis indicates that with the new technique, the cost of a traditional attack is increased by two orders of magnitude." , #7
            'Research is done on keyword extraction based on Word2Vec weighted TextRank':'a research is done on the keyword extraction method of news articles. A candidate keywords graph model is built based on the basic idea of TextRank, use Word2Vec to calculate the similarity between words as transition probability of nodes weight, calculate the word score by iterative method and pick the top N of the candidate keywords as the final results'
            'Similarity Analysis of Law Documents Based on Word2vec':'The similarity analysis of law documents is the basis of intelligent justice, while law documents based on several types of cases are quite different in terms of format and length, which causes trouble in analyzing similarities. For that we propose a more specific approach to dealing with law documents, combining Word2vec with legal documents corpus.'
            'Interpretable Machine Learning in Healthcare through Generalized Additive Model with Pairwise Interactions (GA2M): Predicting Severe Retinopathy of Prematurity':'We have investigated the risk factors that lead to severe retinopathy of prematurity using statistical analysis and logistic regression as a form of generalized additive model (GAM) with pairwise interaction terms (GA2M). In this process, we discuss the trade-off between accuracy and interpretability of these machine learning techniques on clinical data. We also confirm the intuition of expert neonatologists on a few risk factors, such as gender, that were previously deemed as clinically not significant in RoP prediction.'
            'Research on Patent Text Classification Based on Word2Vec and LSTM':'Combined with the features of the patent text, first of all, in the text pre-processing process, words frequently appearing in patent documents such as “the invention”, “involvement”, and “utility model” were added to the stop word list to save storage space and improve efficiency; Secondly, the pre-trained word2vec model was introduced to solve the dimensional disaster caused by the traditional methods. Finally, by training the LSTM classification model, text features were extracted and patent text classification in the security field was performed.'
            'GPS Guided Farm Mapping and Waypoint Tracking Mobile Robotic System':'With the rapid development of automated farm facilities such as auto-weather report, crops growing monitoring,soil testing, animal health tracking, milking etc. a future-focused autonomous real time farm environment monitoring mobile robot platform is in need. Such a system will provide a base for integrating automated farm tools and facilities and maximize the use of modern farm technologies. This research developed an economic GPS guided farm mobile system with the vision for future system expansion. A physical testing model has been built that consists of four major units, i.e. navigation system,communication unit, control system, and mechanical platform. These four units have been successfully integrated as a GPS guided farm mobile robotic system that is capable of mapping and re-tracking field boundaries. It can also be taught by moving the robot around the farm or the perimeter of a paddock to learn the size and shape and gain the environment information for the robot to perform its tasks in later stage. The system provides potentials for further development that could bring more significant contributions to intelligent farming machines and agricultural automation.'
            'Wearable smart health monitoring system for animals':'In today’s scenario, the health of animal has got a lot of concern. To monitor the health of an animal we have to wait for veterinary experts for evaluation and diagnosis. This eventually leads to late treatment and degradation of animal health. Therefore, for primary health diagnosis by the animal owner we have proposed to design a system which tracks the health of an animal. For this we have used sensors such as the temperature, heart rate, the respiratory rate, blood pressure module and electrocardiogram module are used. This can be achieved by developing a system with the sensors which can be mounted on the animal body to get the desired physiological parameters like temperature, heart rate, respiratory rate, ECG and Blood pressure. This system will contribute in the novelty and feasibility of health care of animals. Therefore, a suitable wearable health monitoring system for animals is developed.'
            'Improving Search Result Clustering by Enriching Snippets with Word2Vec Model':'Search Result Clustering (SRC) is an approach to solve the problems of web search engines under users broad or ambiguous queries and no clues to find exact information in a long returned list. SRC groups the returned list and outputs a semantic structured organization to help users to find the desired information quickly.In this paper, we propose a new snippet enriching approach throughout word2vec model. The vector representations of words learned by word2vec models have been shown to carry semantic meanings and are useful in various Natural Language Processing(NLP) tasks. We propose to use the top-n similar words in word2vec model to enrich snippets and we still use traditional TF-IDF weights schema to select features. In order to demonstrate the effectiveness of our method, we design intensive experiments to evaluate new method and baseline methods. The result of the analysis shows that proposed method outperforms baseline approach significantly. '
            'Efficient Video Classification Using Fewer Frames':'Recently, there has been a lot of interest in building compact models for video classification which have a small memory footprint (< 1 GB) [16].While these models arecompact, they typically operate by repeated application of a small weight matrix to all the frames in a video. For example, recurrent neural network based methods computea hidden state for every frame of the video using a recurrent weight matrix. Similarly, cluster-and-aggregate basedmethods such as NetVLAD have a learnable clustering matrix which is used to assign soft-clusters to every frame inthe video. Since these models look at every frame in thevideo, the number of floating point operations (FLOPs) isstill large even though the memory footprint is small. In thiswork, we focus on building compute-efficient video classification models which process fewer frames and hence haveless number of FLOPs. Similar to memory efficient models, we use the idea of distillation albeit in a different setting. Specifically, in our case, a compute-heavy teacherwhich looks at all the frames in the video is used to train acompute-efficient student which looks at only a small fraction of frames in the video. This is in contrast to a typical memory efficient Teacher-Student setting, wherein boththe teacher and the student look at all the frames in thevideo but the student has fewer parameters. Our work thuscomplements the research on memory efficient video classification. We do an extensive evaluation with three typesof models for video classification, viz., (i) recurrent models(ii) cluster-and-aggregate models and (iii) memory-efficientcluster-and-aggregate models and show that in each ofthese cases, a see-it-all teacher can be used to train a compute efficient see-very-little student. Overall, we show thatthe proposed student network can reduce the inference timeby 30% and the number of FLOPs by approximately 90%with a negligible drop in the performance.'
            'Deep Learning Hyper-Parameter Optimization for Video Analytics in Clouds':'A system to perform video analytics is proposed using a dynamically tuned convolutional network.Videos are fetched from cloud storage, preprocessed, and a model for supporting classification is developed on these video streams using cloud-based infrastructure. A key focus in this paper is on tuning hyper-parameters associated with the deep learning algorithm used to construct the model. We further propose an automatic video object classification pipeline to validate the system.The mathematical model used to support hyper-parameter tuning improves performance of the proposed pipeline, and outcomes of various parameters on system’s performance is compared.Subsequently, the parameters that contribute toward the most optimal performance are selected for the video object classification pipeline. Our experiment-based validation reveals an accuracy and precision of 97% and 96%, respectively. The system proved to be scalable, robust, and customizable for a variety of different applications.'
            'Real-Time Adaptation to Time-Varying Constraints for Medical Video Communications':'The wider adoption of mobile Health (mHealth) video communication systems in standard clinical practice requires realtime control to provide for adequate levels of clinical video quality to support reliable diagnosis. The latter can only be achieved with real-time adaptation to time-varying wireless networks’ state to guarantee clinically acceptable performance throughout the streaming session, while conforming to device capabilities for supporting real-time encoding. We propose an adaptive video encoding framework based on multi-objective optimization that jointly maximizes the encoded video’s quality and encoding rate (in frames per second) while minimizing bitrate demands. For this purpose, we construct a dense encoding space and use linear regression to estimate forward prediction models for quality, bitrate, and computational complexity. The prediction models are then used in an adaptive control framework that can fine-tune video encoding based on real-time constraints. We validate the system using a leave-one-out algorithm applied to ten ultrasound videos of the common carotid artery. The prediction models can estimate Structural SIMilarity (SSIM) quality with a median accuracy error of less than 1%, bitrate demands with deviation error of 10% or less, and encoding frame rate within a 6% margin. Real-time adaptation at a Group of Pictures (GOP) level is demonstrated using the High Efficiency Video Coding (HEVC) standard. The effectiveness of the proposed framework compared to static, non-adaptive approaches is demonstrated for different modes of operation, achieving significant quality gains, bitrate demands reductions, and performance improvements, in real-life scenarios imposing timevarying constraints. Our approach is generic and should be applicable to other medical video modalities with different applications.'
            'Delay-Aware Fountain Codes for Video Streaming with Optimal Sampling Strategy':'The explosive demand for online video from smart mobile devices poses unprecedented challenges to delivering high quality of experience (QoE) over wireless networks. Streaming highdefinition video with low delay is difficult mainly due to the stochastic nature of wireless channels and the fluctuating videos bit rate. To address this, we propose a novel delay-aware fountain coding (DAF) technique that integrates channel coding and video coding. In this paper, we reveal that the fluctuation of video bit rate can also be exploited to further improve fountain codes for wireless video streaming. Specifically, we develop two coding techniques: the time-based sliding window and the optimal window-wise sampling strategy. By adaptively selecting the window length and optimally adjusting the sampling pattern according to the ongoing video bit rate, the proposed schemes deliver significantly higher video quality than existing schemes, with low delay and constant data rate. To validate our design, we implement the protocols of DAF, DAF-L (a low-complexity version) and the existing delayaware video streaming schemes by streaming H.264/AVC and high efficiency video coding (HEVC) standard videos over an 802.11b network on CORE emulation platform. The results show that the decoding ratio of our scheme is 15% to 100% higher than the state of the art techniques.'
            'Distributed Video Coding With MIMO for Video Wireless Communications':'The research on Distributed Video Coding (DVC) has been increasingly popular in recent times due to its promising features. In video communications over wireless channels, the noise and multipath fading effects have a significant effect on the perceptual video quality. However, it is noted that in all the research literature on DVC, an errorfree ideal communication channel is assumed. In this paper, we take into account the effects of noise and fading in a wireless channel on the performance of a DVC codec with necessary modifications to the decoding algorithm while proposing a multiple-in-multiple-out (MIMO) based diversity scheme. Simulation results show that the proposed DVC system with 2x2 MIMO channel outperformed the state of the art H.264/AVC video codec at channel SNR levels below 16dB under similar conditions. Further, possible enhancements to the MIMO configuration are also discussed in this paper.'
            'About the Possibility of Integrating Information from Satellite Navigation Systems':'— This article presents the options for the integration of secondary navigation information of satellite navigation systems and the results of modeling the possibility of navigation measurements accuracy improvement during integration. Integration options are based on the method of determining the location of a moving object in space by imposing restrictions associated with the dynamic properties of the object. This method is recursive and is based on the use of secondary navigation information and readings of on-board meters of motion parameters, when each navigation measurement predicts the area of the possible location of the object at the time of subsequent navigation measurements. The corrected location of the object is considered to be the intersection of the areas of space of subsequent navigation measurements with the previously predicted areas of space. As a result of integration of navigation information of satellite navigation systems, the frequency of navigation data updates and the accuracy of navigation location of a moving object increase.'
            'An Inner-Product Calculus for Periodic Functions and Curves':'Our motivation is the design of efficient algorithms to process closed curves represented by basis functions or wavelets. To that end, we introduce an inner-product calculus to evaluate correlations and L2 distances between such curves. In particular, we present formulas for the direct and exact evaluation of correlation matrices in the case of closed (i.e., periodic) parametric curves and periodic signals. We give simplifications for practical cases that involve B-splines. To illustrate this approach, we also propose a least-squares approximation scheme that is able to resample curves while minimizing aliasing artifacts. Another application is the exact calculation of the enclosed area.'
                
}