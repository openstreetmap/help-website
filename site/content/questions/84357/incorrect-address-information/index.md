+++
type = "question"
title = "Incorrect Address Information"
description = '''I live in Bristol, UK and noticed that OSM shows the wrong local area component for all addresses in my road. The addresses all show the local area as &#x27;Kingsdown, Cotham&#x27;, whereas it should be &#x27;Redland&#x27;. This is confirmed as the postal and Google maps both use &#x27;Redland&#x27;. There are two parts to this ...'''
date = "2022-05-04T11:15:00Z"
lastmod = "2022-05-10T09:57:00Z"
weight = 84357
keywords = [ "incorrect", "#wrongaddress", "modify", "error", "address" ]
aliases = [ "/questions/84357" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Incorrect Address Information](/questions/84357/incorrect-address-information)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84357-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84357-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-84357-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I live in Bristol, UK and noticed that OSM shows the wrong local area component for all addresses in my road. The addresses all show the local area as 'Kingsdown, Cotham', whereas it should be 'Redland'. This is confirmed as the postal and Google maps both use 'Redland'. There are two parts to this question: 1. What is the process to contact OSM and have the error above be corrected? 2. Where does OSM obtain its UK address information?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-incorrect" rel="tag" title="see questions tagged &#39;incorrect&#39;">incorrect</span> <span class="post-tag tag-link-#wrongaddress" rel="tag" title="see questions tagged &#39;#wrongaddress&#39;">#wrongaddress</span> <span class="post-tag tag-link-modify" rel="tag" title="see questions tagged &#39;modify&#39;">modify</span> <span class="post-tag tag-link-error" rel="tag" title="see questions tagged &#39;error&#39;">error</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 May '22, 11:15</strong></p>
<img src="https://secure.gravatar.com/avatar/40fabafc0516a3cfe3b45c87c5b24511?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Rich888&#39;s gravatar image" />
<p><span>Rich888</span><br />
<span class="score" title="0 reputation points">0</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Rich888 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84357" class="comments-container">
<span id="84358"></span>
<div id="comment-84358" class="comment">
<div id="post-84358-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Hi Rich. Could you please clarify where exactly you are seeing the wrong address? Do you look directly at the data stored with an object or do you look at the information returned with search results on openstreetmap.org? Could you link to the place?</p>
</div>
<div id="comment-84358-info" class="comment-info">
<span class="comment-age">(04 May '22, 12:14)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="84359"></span>
<div id="comment-84359" class="comment">
<div id="post-84359-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi TZorn, The postcode area is BS66NS, Lansdown Road, Redland, Bristol UK On further investigation, it looks like it is the '<strong>Suburb</strong>' data property which leverages the 'Kingsdown, Cotham' incorrect data. I am not sure where this information comes from but it could be the local ward data which divides Redland and Cotham.</p>
<p>For reference here are the local ward maps for this Bristol area:</p>
<p>Cotham ward reference: <a href="https://www.bristol.gov.uk/documents/20182/4762088/Cotham.pdf/c03c9939-a862-043b-5a14-f9e16990fe9a">https://www.bristol.gov.uk/documents/20182/4762088/Cotham.pdf/c03c9939-a862-043b-5a14-f9e16990fe9a</a> Redland ward reference: <a href="https://www.bristol.gov.uk/documents/20182/4762088/Redland.pdf/a9eb20b2-0b1a-53f2-965a-e09dda6b8fbd">https://www.bristol.gov.uk/documents/20182/4762088/Redland.pdf/a9eb20b2-0b1a-53f2-965a-e09dda6b8fbd</a></p>
<p>The main point here is that the postal addresses for all houses in Lansdown Road and some adjacent roads should be &lt;#&gt; &lt;roadname&gt;, Redland, Bristol, &lt;postcode&gt;</p>
</div>
<div id="comment-84359-info" class="comment-info">
<span class="comment-age">(04 May '22, 12:56)</span> <span class="comment-user userinfo">Rich888</span>
</div>
</div>
<span id="84360"></span>
<div id="comment-84360" class="comment">
<div id="post-84360-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Rich, the suburb is not stored with the houses themselves as you can see for <a href="https://www.openstreetmap.org/way/545355437">15 Lansdown Rd</a> for example. Whatever gives you the wrong information must be drawing it from somewhere else. So let me repeat my question: Where do you see the wrong information? What website or app are you using? What do you do to retrieve the address?</p>
</div>
<div id="comment-84360-info" class="comment-info">
<span class="comment-age">(04 May '22, 13:57)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="84361"></span>
<div id="comment-84361" class="comment">
<div id="post-84361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi TZorn, My apology on the vague answer to your original question. I cannot provide a link to the point of use as this is my company's integration under development. I am the tech writer who has the task of writing a description about the integration. I don't have access to the business OSM account but I can say that the address properties used by the developer are: country, state, city, suburb, major streets, major and minor streets and building. I will pass on your comments to our developer.</p>
</div>
<div id="comment-84361-info" class="comment-info">
<span class="comment-age">(04 May '22, 14:23)</span> <span class="comment-user userinfo">Rich888</span>
</div>
</div>
<span id="84371"></span>
<div id="comment-84371" class="comment">
<div id="post-84371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi TZorn, I've been in contact with the developer and he has shared a link to the map as follows: <a href="https://nominatim.openstreetmap.org/ui/reverse.html?lat=51.46692165316112&amp;lon=-2.6041647791862492&amp;zoom=18">https://nominatim.openstreetmap.org/ui/reverse.html?lat=51.46692165316112&amp;lon=-2.6041647791862492&amp;zoom=18</a> I hope this helps.</p>
</div>
<div id="comment-84371-info" class="comment-info">
<span class="comment-age">(05 May '22, 15:12)</span> <span class="comment-user userinfo">Rich888</span>
</div>
</div>
</div>
<div id="comment-tools-84357" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84357-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="84377"></span>

<div id="answer-container-84377" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-84377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84377-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-84377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The suburbs in your area have only been mapped as node feature (<a href="https://www.openstreetmap.org/node/71050443">Redland</a>, <a href="https://www.openstreetmap.org/node/3207063251">Cotham</a>). The buildings in question only carry basic address information (<a href="https://www.openstreetmap.org/way/545355437">115 Lansdown Road, BS6 6NR, Bristol</a>). So there is no direct link between building and suburb.</p>
<p>The offending data you got comes from nominatim. That tool uses OSM data and guesses the suburb. You can see that when you click on the <a href="https://nominatim.openstreetmap.org/ui/details.html?osmtype=W&amp;osmid=545124261&amp;class=building">details button</a> on the link you gave us. Under the Address heading it lists all suburbs in the vicinity with the distance between the building and the node that represents the suburb. As you can see Cotham beats Redland by a few meters, so nominatim thinks Cotham is the most likely suburb Lansown Rd belongs to.</p>
<p>Coming back to your questions. The information in the OSM database is not incorrect. It is only imprecise as it does not contain the boundaries of the suburbs but only the "center" nodes. As such there is nothing to be corrected. Apparently you are somehow using data from nominatim for your application. It's up to you how much you want to rely on guessing suburbs or not.</p>
<p>OSM is a constantly growing database. It's very normal that objects are mapped with less precision first and then get improved over time. So it's quite possible that at some time Redland will be mapped with its boundaries and the address can be derived with more precision. The suburb could also be entered with the building's address information directly.</p>
<p>You asked "What is the process to contact OSM and have the error above be corrected?". There is none. OSM relies on a large community of voluntary mappers. If you need something corrected or improved you can create an account and do it yourself. <a href="https://wiki.openstreetmap.org/wiki/Beginners%27_guide">It's very intuitive and does not require much learning in the beginning</a>.</p>
<p>Since the problem you are facing is a wider one and not limited to a few buildings you may want to reach out to the local community to check how things could be addressed and how you could contribute. Mapping practices vary from region to region.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '22, 08:52</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-84377" class="comments-container">
<span id="84386"></span>
<div id="comment-84386" class="comment">
<div id="post-84386-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Just to add that UK addressing issues are discussed quite often on the talk-gb mailing list, so that might be a useful place to get more help. For example, perhaps Redland should be explicitly included in the address tags on these buildings, but that would depend on UK-specific tagging conventions.</p>
</div>
<div id="comment-84386-info" class="comment-info">
<span class="comment-age">(06 May '22, 16:37)</span> <span class="comment-user userinfo">alan_gr</span>
</div>
</div>
<span id="84425"></span>
<div id="comment-84425" class="comment">
<div id="post-84425-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi TZorn, thank you for taking the time to help out. The answers are very thorough and helps us understand the thought train, map address raw data sources and calculation approach. The links are useful resources and will assist future development.</p>
</div>
<div id="comment-84425-info" class="comment-info">
<span class="comment-age">(10 May '22, 09:57)</span> <span class="comment-user userinfo">Rich888</span>
</div>
</div>
</div>
<div id="comment-tools-84377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84377-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

