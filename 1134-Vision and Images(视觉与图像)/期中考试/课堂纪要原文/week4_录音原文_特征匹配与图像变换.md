[00:00] 发言人 1: Like sorry mention the image呃， in the last class we have discuss 
how to detect the corner from the image，right？呃，let’s first have some reviews，
right？you remember this，how can we detect the corner from the image？
[00:27] 发言人 1: We utilize actually a geometric structure of a code right that that is 
the age and the geometry structure represented by the age.
[01:15] 发言人 1: Right，so we if we use a a third of plan to cut this structure，we will 
get a case，and that case yes，is what we called in the last class，that it had a long 
and short，and this two acts represent by the lambda。Nice or the number me of the 
parrotic matrix the h is we calculate the eigenvalue of the this matrix is we will have 
a lambda uh the largest eigenvalue and smallest eigenvalue.
[01:59] 发言人 1: 我原来有。And this this two in value represent the variation speed 
along those direction that means if both in value are large no matter which direction 
you move this it will have a very huge variation if this two in value are small both are 
small and it means that no matter which direction you move the change is. All this is 
like the flat flat region and if the it all of the value are around in this region is a 
corner region right and if this one is value is significantly larger than another even 
than this region is an edge that means of the one direction the variation speed is high 
in this.
[02:50] 发言人 1: 哦，商模是在这，啊，那这个我弄在这，然后。depending on. Say，
let’s zoom like this，depending on the geometric structure of this decrease，or the 
geometric structure of the product form，we have found the say，say for example，
the direction of the fastest change and the direction of the slowest change。And this 
two change direction represents we which in which direction the change the 
variation the variation of the difference between two passions is more is have the 
high base speed or the lowest speed. right.
[03:47] 发言人 1: This is what we learned in the last class for the color direction and 
also we have learned that to achieve the scale invariants right how can we do to 
achieve the scale. 六零二。
[04:06] 发言人 1: we. Remember how i achieved that skill in various.
[04:18] 发言人 1: Actually we calculate the exam value along different scale we use as 
the image pyramid right. So calculate the still across the different resolution of all the 
different skills calculate the negative value across different skills and then we can get 
some kind.
[04:43] 发言人 2: of curve.
[04:46] 发言人 1: 对，R is the holder significance，and this is a scale，哎，and we also 
has largest significance corresponding scale。As the representative skill of the of that 
hat of all that corner and this matter we calculate the significance across different 
skill and achieve and by this matter we can achieve the skill because we calculate the 
calculate the maximal. 呃，这个就是 cross of B三 K关系。
[05:30] 发言人 1: These are some basic knowledge we have learned in the last class. 
Then come to the next question. We have actually we have three step at this figure 

right? First to detect the interest word using the a value right? By the last class, and 
then we have to find the description of the export. Please.
[06:00] 发言人 1: Uh，come of features to describe what this corner is or what 
represent the characteristic of this corner，and this is the description，and finally 
their imagination，we have to find the correlation。For example，we have two 
image，which contains many set，a large set of those descriptor of those corners，
they have to build up the。Correlation，这个会很有趣，and this is amazing。So our 
method generally contains following three part three part，and today we will learn 
how to detect and how to match，sorry，how to describe and how to match。Right 
then how can we describe those ports or what the port what the descriptor has some 
requirements.
[06:55] 发言人 2: for.
[07:10] 发言人 1: there may be some basic requirements actually the they are let’s 
say detector we also need the environment of the descriptor. Which mean that our 
descriptor should not vary across for example translation rotation or some other 
transformation and also our descriptor also should be describable that means our 
our descriptor should make the that food be distinguished. Of uh uh sorry to be 
describable of compared with other or other such.
[08:00] 发言人 1: 呃，a a lot a lot other sides of the呃， corners of the insects，that 
means that our descriptions should be highly unique for each and each choice。
Right then we have to find what the transformation we might have in the for a color 
impact for a alignment or for the description task like geometry and photo which 
contains the location scaling and intensification right then be with our units may 
may. Maybe matches maybe such type of changes in that all our description of the of 
the matching process so our description or our description should be invariants and 
this product is. 嗯第三节。
[09:08] 发言人 1: So i really need to look some environment and equivalent detector 
correct this first for the detector we we have already move or we have already found 
the environment and equivalent detector that is.
[09:26] 发言人 1: 应该有基于，你看一下，呃，这个Martin Scale，呃，那个，and also the 
feature dispatcher also designed to be government to those translation rotation and 
scale，and they can already handle some。For example, the limited three rotation or 
limited F E transformation and also the limited elimination of construction. So F E 
transformation compared for example, our translation. The location and the other 
transformation. 这种毫无可能的确认，就。
[10:11] 发言人 2: 发生在。
[10:14] 发言人 1: First actually we should make our environment，and then we can 
design an investigation descriptor。Some maybe use some feature descriptor for 
example we can directly use the pixel value right and then we can also use the 
window of the pixels then local window or three times three window to this to this to 
this feature but how can they achieve for example the first location. 一般。How can 
we change the truth across地方。地方是黑色往地方的门口。

[11:30] 发言人 1: right，比如呃，still remember for the coffee interaction，right，they 
have that kind of quadratic form，that you play，然后。
[11:53] 发言人 1: And this major stage actually described as. This part describes the 
local geometry of a difference of a base difference UV and its difference. It tells out 
the difference between two patches.
[12:20] 发言人 1: 啊，我们不不不，and this it represents呃 increase and and last part 
the starts and this actually this increase has呃 two important direction that that 
made a long as and short radius right this this two directions actually。Right it’s 
much better the exactly value is not value. That means the last of this in case.
[12:57] 发言人 1: The readers of this details has been not value, no matter how you 
rotate this, how rotate this local patterns, right? This and the length is the one right 
by the one me and all the one max so we can come to a method that utilize this local 
structure of the age that we can for example if this image is ok it actually they can 
delete this ok. 哎，但是 the length of short value the corresponding angle 不 change 
right this theta or now it may calculate the theta of this two lengths right the the 
same same theta 不 change so we can actually rotate this long s back to the two.
[14:00] 发言人 1: 后来做的时候，但是我的。If this ellipse is rotating along for example 
the origin for a certain angle，but the corresponding geometry of all structures 
remains，so we can rotate this line back to the horizontal plane，and all the 
structures remains，so we can utilize this rotate back。Structure to describe the 
local therapy of this type，and then this can change this this location，so the method 
is given a x max，in the matter of the said woman missions is。哎，CC.
[14:51] 发言人 1: We can do this correspond the investor correspond to the longest. 
That is the X max corresponds to the number map and then we can simply rotate this 
patch back to certain degree for example we can rotate all the the largest invalid 
vectors back to the horizontal or back to the vertical so we can align all the structures 
in the same direction. And she achieved the problem you are right that means they 
may have a lot of key.
[15:33] 发言人 2: points.
[15:35] 发言人 1: like this or like this. 哦，原来。来 C还有低端的，有 K M。We have 
noted this at stage example to the oracle dump你看左边这一排，是 oracle dump。And 
then we can compare those structure and see or not.
[16:10] 发言人 1: because they have enemies呃 relative location between those 
different equals because this this x is该该什么呢。 That that’s a process is like this 
given by the largest呃 given by the even better corresponding to the largest even by 
they have simply ordered of the creations. All the rotated patch according to that 
handle and utilize this rotated patch to describe those local padding and this can help 
us achieve the rotation in that.
[16:55] 发言人 1: 包括你看这边在业务端谁可以跟大家。然后现在这个。So the many still 
there has a many still oriented patches descriptor that means we can for example we 
sample a square window around the detection feature we have still two different 
sides and located it for for double and vertical and then sample a square window 
center as a feature. And we have we have also normalize this vector by subtracting 

the mean and division by the standard because here you know why we have the 
interview this normalization.
[17:54] 发言人 1: 然后所以还有这个both geometric and photo metric. These two wells 
we have to achieve the both geometry geometry and formation in wells and so here 
we apply the normalization is to add in the formation vectors.
[18:20] 发言人 1: And then we can detect the呃 the descriptor at my skills like this 
image. 啊，here is still very figure some errors。And to achieve the scale 
environment we can do the image parameter as a formation with a parameter the 
same as of these characters of more different skills and then find a close skill to tell 
the structure and the scale environment features transformation.
[19:00] 发言人 1: That the six will not be by cutting a large patch to a very small 
patches and then it’s calculate the orientation of different small patches and make a 
histogram that make a statistic and then utilize because if. Sometimes the pages 
rotate the direction of the this pistol brand is just shift by different number for 
example start with zero or start with half half title start with two million there there 
is just a shift between different number so it utilize the largest. In two they think the 
bees make the biggest one at the start so it can also achieve the rotation environment 
because it’s shaped the biggest bee in the in the first.
[20:01] 发言人 1: That is designer is here both scale and rotation feature。basic idea is 
that like here take a large square window呃 around the different features and 
compute as orientation for each so。Then it threw out we make enemies and create a 
histogram that means make a statistic of different angles of this patches and then 
make a make a histogram like this and the practical step is to shift the B as the 
biggest slot. because if you do not shoot it’s may contents嗯 the cases that the 
patients are the same but it’s no cases so the start may be this one or start with this 
one. Make all the the combination of the biggest and the first it’s time make it’s 
kind of change this locations in America because you all always make the biggest one 
first。
[21:19] 发言人 1: Then there is over to achieve the strong environment that provide 
you window to focus on results and then compute our teachers grant of excuses and
最后来说，呃，longer histogram that is sixteen sixteen sales times is coordination to. 
啊，a hundred and twenty eight，quite high high high in this question。And here is 
some profile of the shape. That means it can handle the changes in the real world, it 
also can handle the significant change in the information, and it’s pretty fast, hard 
to make real time.
[22:24] 发言人 1: one and他 also also simple but really useful or the this this. The 
corresponding point are that’s a line also like this region or like this region 
corresponding point are also a line all is this region or this region right all this just 
simple right it only means that this is.
[23:12] 发言人 1: Here are some third. And there are some other descriptor like 
histogram of the green all the track plus the keypoints defender all the lift. And we 
have also the hazel brand hazel brand computer horizontal and vertical brilliance 

and it’s type with the brilliant magnetic orientation at each pixel and this also that 
they use the c o p program and give very many things most else and.
[23:52] 发言人 1: 告诉黑黑子过来，我多一点到，告诉朝人黑神。Then we can more than 
we can more than. 接近的和送端啊，保守的端。我我玩密秘的。
[24:14] 发言人 1: It you the fast color texture and compute independently determine 
determine the orientation it’s you like a circle texture you have a circle feature to 
determine the color and the. So determine the orientation and get the time. Part for 
the detection and describe for the detection actually we generally focus on the corner 
detection and its expansion is the harvest.
[25:00] 发言人 1: The color detector utilizes this this structure is the structure is and 
the largest and smallest in the value is the most important information for the color 
detector the color detector. 呃，look at most largest and smallest quarter to to呃
largest smallest呃， exam all the comparison between those two exam。And also for 
the disruption most important is that same thing you like this program also this 
program of not only oneself but a many catch of.
[26:00] 发言人 1: Stand by cash to cash to to get a high dimensional description of 
local vision. Nice and takes a little example also indicated that the alarm is really 
useful for the actual alarm. S.
[26:32] 发言人 1: 同期。The another question is actually how can we get the price 
feature match? Here are the feature in the the first image, how can we find the best 
match of the second image? Right, like the example we have. 出三条货就行。
[27:15] 发言人 1: We have those-Pacific food，how can we determine whether this P 
one is a line through this or this or this？But how can we determine whether one 
should launch the which point on the other side? Yes, our feature the feature 
description or description already come up, we have a vector question.
[27:44] 发言人 1: For each word, we can use a vector to describe this word, and then 
we can actually find which description for the second size is the. 你的三餐还有个。The 
similar description with this first point and then combine the proportion between 
the features or the food is the I one and the I two. So our first class is to define the 
distance function so that we can describe, we can compare the descriptor or we can 
compare the.
[28:24] 发言人 1: Expression of those two sets of books，right？We have to first to find 
a distance function，and then we have to test all the features on the，it seems like a 
really right，we have to find all possible values and find the smallest one。Then we 
may test all the features on the in the i two and find one with the minimum distance. 
哎。这是奥特曼卡，按照这个。
[29:18] 发言人 1: And then we can get give small distance books. Sometimes both 
maybe both we have different concept but has a very similar distance. Then we can 
further look like ratios between. 这都是第三次，哎，面呢，哎。
[29:41] 发言人 1: One distance is significantly lower than others means that we have 
more confidence on that similarity but if two process and very similar distance 

distance or the the ratio of the distance. 这个 twenty two and two one in the. The the 
changes of the our confidence on the alignment is also high。
[30:14] 发言人 1: This is the initial distance or this is absolute simple distance。So. S S 
D。compare to the reason is actually嗯 sometimes can not find the嗯 best one or can 
not嗯 find.
[30:42] 发言人 2: the嗯。
[30:46] 发言人 1: That’s that’s not all food same result class exchange this time 
let’s change office ok.
[31:07] 发言人 1: Or flyer and then the last part is how can we evaluate those results 
right how can we evaluate those results we may find a metric or find a matrix to 
evaluate those results right. Like here, maybe calculate some distance like fifty, sixty 
five, seventy five of this one. And the first two are true match and the second is false 
match. Sometimes they they they are very important construction that is a true 
politics and false politics the true politics. Here it’s need that the detector is rightful 
which are right and also you detection is the right that means you if you know the 
real detection is not the right and you the else some tell you you detection is also 
right and then this kid is the true quality and the false quality is.
[32:26] 发言人 1: 那个呃，totally opposite with that，you the outer some cold，this is 
incorrect，and actually really incorrect，so this is the force of this，this force。啊第
二个呢第三头。啊。哎，our site has a thousand matches and eight hundred are prime 
match and two hundred are equal。AND EL EL ELIZABETH TELL US THERE IS A SIX 
HUNDRED CHRISTMAS AND A HUNDRED IN CHRISTMAS. Then what is the true 
quality and the false quality?
[33:28] 发言人 1: The true point is we provide our awesome car six hundred one the 
total price eight hundred. Uh，we are going to equate the sixty five percent and the 
whole quantity with one hundred，divide by two hundred。
[33:48] 发言人 1: As you may think，there is some problem，as why the our device 
there is only sixty six hundred phones，but the whole function。稍微的做些。So why 
the small machine of the all all customers to our our small people is the whole food 
because in the in the in the. yes.
[34:32] 发言人 1: Why this happen actually this costs i i also actually not behind the 
revenus three hundred four so only all seven hundred four this is also another. The 
reason of the.
[34:51] 发言人 2: increase.
[34:54] 发言人 1: and the second important curve that is called the. R.
[34:58] 发言人 2: C.
[35:01] 发言人 1: The our thinker that we vary the threshold in our algorithm and then 
we draw the line of cost about the false positive rate and the true positive rate and we 
can draw this our thinker right it will vary the. 呃，是 I code for the for our 
algorithms and then the and then outside curve is called the several of the algorithm 
and then it also our calculate the A U C A U C in every under this curve。

[35:39] 发言人 1: 第三面积，这个面积的area along all the curve in this in the in the 
three in the. And then we have a great place to summarize summarize. 百十二十五。
Match distance and different threshold we can average that matches with different 
true or false positive rates and auc is very by continue rate and set of threshold value 
and auc summarize the performance of feature判断。 And also we have different 
application like the construction or the construction or the renovation or the 
education.
[36:39] 发言人 1: Oh, very nice.
[36:49] 发言人 1: 啊，这里你看，呃，一定要功能性的一个过来，就是actually the manual 
feature from actually。
[37:06] 发言人 1: Maybe more accurate like this feature of this end by the then feature 
we can simply have a language change one in base and another video of graduation 
or we can just and this lines are calculated in the.
[37:32] 发言人 1: And also some features. That across some largely exposed with. Like 
this, you know.
[37:49] 发言人 1: 如果这样，上面discussion，我们也可以。Okay，Does this matter？We 
have finished the learn part of matching and description and matching of the image。
In this class we have learned how to behave and how to describe the future by the 
discussion discussion discussion and the answer is by the common behavior of next 
domain structure and.
[38:45] 发言人 1: I you you look at the loss function of this and one and another and 
other.
[39:10] 发言人 1: 嗯。喂，龙龙，那现在还有小玲，free.
[39:17] 发言人 2: 还有潘乔，北京。
[43:55] 发言人 2: 没有够啊，不够。
[45:02] 发言人 2: 让我电话说有。
[45:19] 发言人 1: 人都不定来一袭。
[45:58] 发言人 2: 这个表格是这样的。
[51:36] 发言人 1: ok.
[52:19] 发言人 1: 嗯，就是那个 486 嘛，啊，因为 4186 还没发错吧。
[52:24] 发言人 2: 4186，对，就是 4186，对啊，应该是吧，发错了也不是我们的事情。
[52:40] 发言人 1: 老师这边没卷子。
[53:41] 发言人 1: 给我发Email。
[54:00] 发言人 1: You can submit a paper a white paper with your name and then you 
have send your answers to my email address ok you bring the computer.
[54:48] 发言人 1: right the the student without the quick paper have send the email to 
address right but if you have paper you must submit your呃 quick paper ok if you 
don’t. Paper you can run your name on a white paper.

[55:23] 发言人 1: 完成。
[55:30] 发言人 1: 老师，这email课上发了吗？对对对。 You have to submit you have 
submit email in also in the thirty minutes without this time limitation without time.
[57:55] 发言人 2: 是。
[59:16] 发言人 2: 一倍。
[60:06] 发言人 2: 我想。
[62:55] 发言人 2: 是。
[64:00] 发言人 2: 嗯。
[64:46] 发言人 2: 但是。
[68:27] 发言人 2: 那。
[69:00] 发言人 2: 啊。
[73:38] 发言人 2: 就。
[74:08] 发言人 2: 保持。
[74:56] 发言人 2: 好。
[76:49] 发言人 1: 啊。
[81:06] 发言人 1: 的颜色。
[81:54] 发言人 1: 嗯。
[82:01] 发言人 1: 啊。
[83:34] 发言人 1: 呃，一般三年级就就这个啊，对吧？
[83:54] 发言人 1: 无聊。The this class will learn how to transform image and do the 
image working. 呃，你的 last class，然后我们来讨论一下，说 like this figure to behind 
the corner and describe the people and then to the machine，after to the machine 
we will get the speech of this image，that is combine all this image into a single 
larger view，right？满意支持啊，只要那 how to work。Or how to command speaking 
transformation so there different transformation of image like the translation. 这个二
型传播一些 F E传播一些， or projecting传播一些，然后 in this time we will learn all of 
these transmissions。First，let’s say that a，you should give me，呃，basic 
example，this two unit，this simply，我刚才 standing for two unit，拿。
[85:14] 发言人 1: From the initial results we can see that apparently we can not simply 
stacking those three days together. But move but the inherently reason is that there 
are some structures around here this line should be the color or exactly same with 
those part but actually they get crossed at the same way right. there is.
[85:57] 发言人 1: how can we do this kind of transformation. right they are two people 
we need first know what’s the transformation exactly is and can help us to do this 
and then we need to know figure out how to compute those. Translation parameters 
and do the matching these are two components right there are first we have the 
image filtering that’s take a change the region of the image.

[86:32] 发言人 1: 啊，新新的另一个。Like this we have also the even working they 
change the domain like this. They are very simple transformation and also has a 
location transformation and science transformation that say for the year working 
order we need to first for all the two problems. We are first at the basic mathematical 
of the translation like this.
[87:07] 发言人 1: How can we communicate this kind of transformation? Thus we can 
simply calculate the pixel of each from the original image然后 like using a 
transformation missions可以 using transformation missions key we might go with 
the original pixel location XY今天这个 X com Y com这个新。他说我们的呃非洲嗯
location，爱情。And here we give some example for the scaling right for scaling we 
can simply change the.
[87:58] 发言人 1: 八十。扣减你的team和 interface。现在我们可以看，directions as 
corresponding value has one divided by s and the other is all divided by s。And also 
we can set the rotation matrix here, cosine theta, sine theta, cosine theta, this makes 
the image rotate with the original clockwise or counterclockwise, right? 就是
remember that theta that is actually theta not she theta for the universe is actually 
the universe of this rotation matrix is actually the transport of this if you can 
compute the r with the r controls we can see the similarity calculation.
[89:00] 发言人 1: Yeah，And then for music，so it means the transport of the art is the 
universe rotation process。嗯。We also have the matrix population like this.
[89:19] 发言人 1: 怎么用啊？我猜。Like this and you can also that it may never across 
the line one equals x equals like that. And here the two D translation does carry use 
the two D translation right information transformation we use the missions.
[89:57] 发言人 1: X Y.
[90:08] 发言人 1: But have we also have the same transformation to describe the 
transformation that is the s plus t x y plus t y and this transformation. representation 
by呃 matrix multiply with x y vector。
[90:38] 发言人 1: 嗯，刚才已经弄，应该是没看到。Because they will can calculate the 
result as this each term should contain this some character嗯，就是 results the x call 
y call equals to。Comparing the multiple multiple with XY but we can construct X 
plus Y plus construct.
[91:08] 发言人 1: 作为例周一这六次的进一步的，and here we first discuss characteristic 
of the two B transformation the promoted like that origin maps origin like mouth那
个传输力呃 transformation还有那个。那点什么呀？嗯，我们共同派 scaling operation，
so the ordinal matches the ordinal，and the line matches one，parallel line，
parallel，and we show that they work，they have a close on the competition，right？
They mean that we have，compile in the merge，if on the basis of a single one。再来
一个什么 A V S好的。那中心也是高的那些爱的。
[92:00] 发言人 1: Further variation here the original variation XY homogeneous has a 
perfect one to this matrix and the resulting matrix is XY one that is three also 
converted. Calling it to the homogeneous quantity like here the x divided the w and y 
divided up and we can normalize to transfer to the homogeneous quantity means this 
homogeneous quantity we can actually achieve the calculation right. If we say 

transformation matrix and also a three dimension three to uh three times three 
matrix and we can simply construct the transformation matrix like this one zero t x 
zero one t y zero one as. iphone six six那个 X Y one给他盖的可以啊。产业关系，所以这
个 graphic的管理机制，我们也是呃，我们也是从。
[93:18] 发言人 1: And here we should in here we could further transformation system 
that is transformation transformation have two keys so last呃 the last one has zero 
zero one ok. Last week，and zero zero one，if we came that zero zero one，we can 
tell that such kind of transition，no matter what element on the factor，g c a c d，no 
matter what value on this，they both transformation啊。 O I D传输。
[94:26] 发言人 1: And here is the property of the ethnic translation. The origin are not 
nicely matched because we introduce the translation and that has none. Problematic 
with one color. Race show that preserved and clothes are under competition. And 
this is.
[95:14] 发言人 1: Because the identity matrix should keep the parallel line to be 
parallel also the unpolar line to be unpolar however this is that both two lines 
actually not parallel but on the merge will it becomes the same line it is parallel to 
the same line so. Here is a further modification for that mix and match that we do 
not care the last one has zero work. And here for the F eight transmission，呃，so 
here for the two graph，这里。
[96:02] 发言人 1: This is a photographic reason of protecting like this all the three part 
all the A part in C E I P H R呃，心月楼， right but they was also keep the last and one. 
And here is the results for the home run with transformation. And here is actually 
some insurance in the home run.
[96:34] 发言人 1: We should know that there is a key value is a dominator. The 
dominator is the last row multiple with this. 嗯，X Y Y，X Y。And the results is a is 
this domain is called the domain.
[97:00] 发言人 1: So as the dominator approaching zero because we have to normalize 
right we have to normalize this vector x y w equals to x y is divided by the w but here 
is some kid that in the dominator approaching zero you’ll see that x divided by. Why 
is right down this right will become extremely large so this will turn that there as a 
monitor value approaching to zero. near the the position the x y the target distance 
for the the distance. And the early in the spring meets exactly on the branch and in 
the terrible plants in the original image will meet the branch.
[98:13] 发言人 1: And here are some example for image working like this they will try 
some apply working all the time image like this we will we can convert the original 
underline to the parallel as the market and also generate some unthinkable. Since 
appear that is. This is the homographic transformation and the homographic 
transformation have only property that origin does not necessarily match the origin 
and life matches to life every life does not necessarily match racial process and that.
[99:10] 发言人 1: Then we can track the good black summary of this relationship of 
the translation X T Y it has two degrees of freedom for the region or clean we add a 
location and the you and this way very three because. The location matrix only has 
one degree of freedom啊，加这个 c呢，关系。所以， total degree of freedom is three，

and for the mechanical transmission，the degree you have，because we have further 
scaling，yeah，the scaling，and for the i means are made in. 整另外的 sex of all the A 
B C音乐。
[100:09] 发言人 1: And here we also introduce to give it watching happy that is a phone 
one work and a tablet work give it a list right. The forward for example we have a 
image and also a target image.
[100:34] 发言人 1: 啊。
[100:42] 发言人 1: Attire image, all the image.
[100:51] 发言人 1: And we calculate the translation of that pixel. We translate this pixel 
to. Another location, but this location may not fill in the exactly way. Maybe on that 
location, it’s not filling an exactly. Remember you can work the location one two 
two the location one two five.
[101:24] 发言人 1: So here you need to interpolation，通常 interpolation，然后你开始 
work，一般 to pull now around this pixels and do the aggregation all the interpolation 
all this。然后呃 on structured target to our the real on great point right maybe to 
interpolate this point. Uh using the projected projected point from the original this is 
a forward forward and means.
[102:00] 发言人 1: Our target our transfer pixel will not located on exactly green and 
we need to do the after the transfer. Like like this like this image our target or our 
original pixel is located like here after calculation is located like this but this book is 
not on the exactly book so we need to do the inflation in the place on on grade. 
Coach.
[102:48] 发言人 1: 老板没有，还有好多都做的引味说，咱就是，他们需要干的，exact pixel，
G S right from this corresponding location。此外，the universe working made that 
we know we have to start from the transferred or transformed image of pixel 
location. This pixel is exactly on the grid, and it will transfer this pixel location back 
to the original image.
[103:21] 发言人 1: And but you know that this thing of the vision may be not on the 
exactly grade so we should do the interpolation on the original image interpolate the 
pixel value on that location and then transfer it back to the pixels on the image this is 
called the universal. Like here we we know the targets the real the target position of 
the of the our transformed and then we that is back to some where is on where is 
location on the original. And do the interpolation on the original image to transfer 
pixel location to transfer pixel value back to the working digital universe.
[104:12] 发言人 1: So there are basically there are basic differences in do you do the 
interpolation on how do you do the face value. Building on the original on the 
polynomial of the transformed image or on the original image if you put the 
polynomial on the original image this is invertible but if you do the polynomial on 
the transformed image this is invertible. And there are some basic method near 
neighbor near pixel to define pixel of our careers and find in there to be. right ok. 嗯，
那那个好处看，我们应该 ok。
[105:19] 发言人 1: 没得啊，赶紧完成。嗯。And more than that, I will try to your.

[108:49] 发言人 2: 哎呀，好意思。
[111:19] 发言人 2: 你是要修地线，你那个本身的功能就是怎么样？
[112:09] 发言人 1: For the tomorrow session by P H D student mister李倩哲 will teach 
us how to apply the knowledge learned in this course to our python code manual. To 
realize this process ok the mississippi is an expert in the and tell us.
[115:17] 发言人 3: 啊，我记得我有个店。
[115:19] 发言人 2: four o’clock.
[115:22] 发言人 3: 四四点钟呗。
[115:24] 发言人 2: 大家可以看休息方式。
[115:40] 发言人 2: 前期。
[117:25] 发言人 2: 的技能。
[117:34] 发言人 2: 还需要。
[117:55] 发言人 2: 洗衣机。嗯，开发一个。
[118:34] 发言人 3: 嗯，hello everyone，here we start our future of war，因为 matching 
and transformation，and the teaching assistant，张天德。啊，今天嗯 cover by the or 
key concepts feature detection description using S F T。嗯本来听的那个万一听。
[119:00] 发言人 3: matches using variance and is criminality and parametric 
transformation rotation scale translation and then the earth in a working for 
alignment. First we need to remembering and something that is future environment. 
We applied geometric transformation such like uh rotation by or.
[119:29] 发言人 1: uh.
[119:30] 发言人 3: zero point five times scale and then we extract the S I T that is still 
Americans feature transforming transform we extracted the saved keypoints and 
descriptor composing images. And the match calculate the percentage of the sample 
match is learned environments. The saved means returning to which location to 
make the.
[120:00] 发言人 3: In place that first day you have keypoints and generate descriptor 
for each keypoint typically a rapper and then perform the feature matching by 
comparing the similarity because it was very much practice here’s a close. 嗯，人体
的因为爱情。We need to extract the descriptors for two overlapping images and use 
the key neighbors.
[120:31] 发言人 3: imagining the key equals to and then apply the noise review pass 
pick the match and then realize the millionaire matches. K K因为都意思是 find two 
candidate descriptor that are most similar to the original descriptor here is our 
original photos. And then those green lines are those matches.
[121:00] 发言人 3: 嗯，从go to，we can see that呃， the those points in the realizes 
means people in the same place。感觉是够。And then the third progress we need to 
image working alignment we need to extract the coordinates of the master people 

from the two images and estimate the overall work with high metrics using plan set 
is the random sample concerts.
[121:34] 发言人 3: The whole world is the three model people three matrix that 
describes the countless between point location of the two different viewpoints. Here 
is a figure we can see when I see and then we can work in one into the perspective of 
into two using the home work and narratives and then create an overlay. 呃 word.
[122:07] 发言人 3: Here is the output of the of the of this of this algorithm. You can see 
that it’s a hard perspective that the target image is two. And then in the middle is 
the one we work.
[122:25] 发言人 3: They identify using photo working and the black area means there 
are no pixels. That’s the track from one. Here we can see the perspective work in 
one, and then we overlay both of them.
[122:42] 发言人 3: The red means the work in one, and the side means in two. We can 
really affect the alarm, the alignment differences. 感觉都透以前他跟。或者三个。
[123:07] 发言人 3: This cover box has a slight difference between you and your clothes. 
ok ok，那到时候来，到时候六点四，百分之四十，到时候。
[123:39] 发言人 3: 二P S二 P S这个就是他的。哦， as the pictures use a real code，the 
the feature has some mistakes，所以 I changed you have。嗯，这个意思。
[123:55] 发言人 1: 呃。
[123:57] 发言人 3: I think the picture is correct啊，可以。
[124:14] 发言人 1: So we are.
[124:23] 发言人 1: 所以我们。啊，对，是个精神。你这样应该升级啊。
[124:39] 发言人 3: 就可以是吧？可以。
[124:43] 发言人 2: 对。
[124:52] 发言人 2: 嗯。
[125:49] 发言人 2: 嗯。
[126:55] 发言人 2: 嗯。
[127:50] 发言人 2: 对。
[129:01] 发言人 2: 客户。
[129:52] 发言人 2: 不挺深圳。
[135:39] 发言人 2: 嗯。
[136:50] 发言人 2: 嗯。
[137:55] 发言人 2: 嗯。
[141:01] 发言人 2: 嗯那个你有没有认错啊那个我说你你以前是哪个学校我说有没有认错有人
认错哦那个可能认错了不好意思哦我是北北化的哦。
[141:35] 发言人 2: 嗯。
[143:25] 发言人 2: 嗯。

[144:31] 发言人 2: 嗯。
[145:11] 发言人 2: 嗯。
[145:59] 发言人 2: 嗯。うん。
[146:37] 发言人 2: 啊。
[147:33] 发言人 2: 啊。
[148:05] 发言人 2: 嗯。