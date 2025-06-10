+++
type = "question"
title = "What key &quot;shop&quot; includes?"
description = '''Hello,  I would like to know if the key &quot;shop&quot; includes individual shops or buildings that can have many shops. For example:  Can a shop being a shopping center? Or it will give back all the shops within a shopping center? If there is a big tesco with pharmacy and clothes shops inside, will the key ...'''
date = "2021-02-17T15:40:00Z"
lastmod = "2021-02-17T18:49:00Z"
weight = 78901
keywords = [ "shops" ]
aliases = [ "/questions/78901" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [What key "shop" includes?](/questions/78901/what-key-shop-includes)

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
<span id="post-78901-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78901-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78901-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I would like to know if the key "shop" includes individual shops or buildings that can have many shops. For example:</p>
<ol>
<li>Can a shop being a shopping center? Or it will give back all the shops within a shopping center?</li>
<li>If there is a big tesco with pharmacy and clothes shops inside, will the key "Shop" return only Tesco or it will return the shops within it as well?</li>
</ol>
<p>Thank you. Catherine</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-shops" rel="tag" title="see questions tagged &#39;shops&#39;">shops</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Feb '21, 15:40</strong></p>
<img src="https://secure.gravatar.com/avatar/78ca4faede71449fd93c1790b87d816d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Katerina_Kourou&#39;s gravatar image" />
<p><span>Katerina_Kourou</span><br />
<span class="score" title="26 reputation points">26</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Katerina_Kourou has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78901" class="comments-container">
<span id="78904"></span>
<div id="comment-78904" class="comment">
<div id="post-78904-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hello,</p>
<p><a href="https://help.openstreetmap.org/users/10133/tzorn">@Tzorn</a> <a href="https://help.openstreetmap.org/users/8468/sekerob">@SekeRob</a> Thank you both for your answers.</p>
<p>Can I ask an additional question? I'm using the package pyrosm in python and I'm getting all the shops with pyrosm.get_pois (points of interest). If I tag for all shops, I guess this will give me malls and department stores as well as individual shops? Or POIS means only individual shops and in this way I avoid including malls as well?</p>
<p>Thank you, Katerina</p>
</div>
<div id="comment-78904-info" class="comment-info">
<span class="comment-age">(17 Feb '21, 17:11)</span> <span class="comment-user userinfo">Katerina_Kourou</span>
</div>
</div>
</div>
<div id="comment-tools-78901" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78901-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="78902"></span>

<div id="answer-container-78902" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78902-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78902-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-78902-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Katerina,</p>
<p>I suggest you read up a bit on the topic in our Wiki. Have a look at the general <a href="https://wiki.openstreetmap.org/wiki/Shops">shops page</a> as well as the <a href="https://wiki.openstreetmap.org/wiki/Key:shop"><code>shop=*</code></a> key and the <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Dmall"><code>shop=mall</code></a> and <a href="https://wiki.openstreetmap.org/wiki/Tag:shop%3Ddepartment_store"><code>shop=department_store</code></a> tags. Also look at the discussion pages there for hints on tagging.</p>
<p>You ask about what shop is giving back or returning. Are you asking on how to use some search engine? Which one are you talking about? There are different tagging approaches and a differing degree of details mapped out across our world map. So it is difficult to answer if a pharmacy inside a Tesco would be tagged separately or not. You will probably find both.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '21, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ddebc8d5f4e0458413eacf65e36561a9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="TZorn&#39;s gravatar image" />
<p><span>TZorn</span><br />
<span class="score" title="12350 reputation points"><span>12.3k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="225 badges"><span class="bronze">●</span><span class="badgecount">225</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="TZorn has 63 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-78902" class="comments-container">
&#10;</div>
<div id="comment-tools-78902" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78902-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78903"></span>

<div id="answer-container-78903" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78903-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78903-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78903-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is e.g. shop=mall encompassing all as additional tag to a building marked as e.g. retail or commercial to note a few which then could be called the name the mall was given. Then it's up to the mapper to choose creating the individual points of interest (POI) and place them as close as possible within the building outline as to where a shop can be physically found to include if you'd include their mail addresses add the tag addr:floor = n (so happen to do that today). These POI should not be put on any building line, you'll be told to extract them again and move them in a free space. Certainly I'd not tag the whole building with a name like Tesco if Tesco is just a part.</p>
<p>In the extreme you could map each individual shop in a building and then bind them together in a relation but do not remember to have ever seen this done.</p>
<p>@ Tzorn, over here there's the big Conad chain which runs sub businesses such as the branded Parafarmacia Conad. These are put in a separate POI within the Conad area of operation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '21, 16:22</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Feb '21, 16:28</strong> </span></p>
</div>
</div>
<div id="comments-container-78903" class="comments-container">
&#10;</div>
<div id="comment-tools-78903" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78903-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="78907"></span>

<div id="answer-container-78907" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-78907-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-78907-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-78907-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Think of the building as a box(the shop=mall), then you arrange the shop POIs in that box. horizontally or vertically (the floors). If they get too close of each other they wont render, but the data is still there.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Feb '21, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/ed39ace8cbefe3b5c45da98f60f5e34c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SekeRob&#39;s gravatar image" />
<p><span>SekeRob</span><br />
<span class="score" title="211 reputation points">211</span><span title="19 badges"><span class="badge1">●</span><span class="badgecount">19</span></span><span title="20 badges"><span class="silver">●</span><span class="badgecount">20</span></span><span title="27 badges"><span class="bronze">●</span><span class="badgecount">27</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SekeRob has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-78907" class="comments-container">
&#10;</div>
<div id="comment-tools-78907" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-78907-form-container" class="comment-form-container">
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

