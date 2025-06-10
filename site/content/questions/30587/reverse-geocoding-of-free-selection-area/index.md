+++
type = "question"
title = "Reverse geocoding of free selection area"
description = '''Hi,  I have discovered a possibility to get addresses of a map area.  The first thing that should be done is to create an Area via http://www.openstreetmap.org/edit#map=  After it has been save, I can have the id of this area (example: http://www.openstreetmap.org/way/260934781) But when I try to to...'''
date = "2014-02-10T15:35:00Z"
lastmod = "2014-02-12T12:11:00Z"
weight = 30587
keywords = [ "reversegeocoding" ]
aliases = [ "/questions/30587" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Reverse geocoding of free selection area](/questions/30587/reverse-geocoding-of-free-selection-area)

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
<span id="post-30587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have discovered a possibility to get addresses of a map area. The first thing that should be done is to create an Area via <a href="http://www.openstreetmap.org/edit#map=">http://www.openstreetmap.org/edit#map=</a> After it has been save, I can have the id of this area (example: <a href="http://www.openstreetmap.org/way/260934781)">http://www.openstreetmap.org/way/260934781)</a> But when I try to to compose a request to get the addresses of this area, I get</p>
<blockquote>
<p>This XML file does not appear to have any style information associated with it. The document tree is shown below. &lt;reversegeocode timestamp="Mon, 10 Feb 14 15:31:59 +0000" attribution="Data © OpenStreetMap contributors, ODbL 1.0. &amp;lt;a href=" http:="" www.openstreetmap.org="" copyright""=""&gt;http://www.openstreetmap.org/copyright" querystring="format=xml&amp;osm_type=W&amp;osm_id=260934781"&gt; &lt;error&gt;Unable to geocode&lt;/error&gt; &lt;/reversegeocode&gt;</p>
</blockquote>
<p>Please give me a hint what can be wrong?</p>
<p>Thank you!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-reversegeocoding" rel="tag" title="see questions tagged &#39;reversegeocoding&#39;">reversegeocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Feb '14, 15:35</strong></p>
<img src="https://secure.gravatar.com/avatar/22e328d0339246bdc6e0fbdcfa80141c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SaleksV&#39;s gravatar image" />
<p><span>SaleksV</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SaleksV has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-30587" class="comments-container">
<span id="30589"></span>
<div id="comment-30589" class="comment">
<div id="post-30589-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Please don't create areas such as <a href="http://www.openstreetmap.org/way/260934781">way 260934781</a> that don't actually refer to anything in the real world!</p>
<p>It would help if you could describe the problem that you're trying to solve first, rather than how you're trying to solve it (that doesn't work). So - what is it that you actually want to do?</p>
</div>
<div id="comment-30589-info" class="comment-info">
<span class="comment-age">(10 Feb '14, 15:40)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30596"></span>
<div id="comment-30596" class="comment">
<div id="post-30596-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, SomeoneElse Thank you for understanding. I would like to use your service for one purpose. Please see step below. 1. Open a map. Navigate to required area. 2. Select some certain area, which includes some buildings. 3. Store this area with some name and have a possibility to access this area in order to read/edit/delete. 4. Have a possibility to extract all addresses present on the area (street number/housenumber and other information). That is the problem. Looking forward for your help! Thank you!</p>
</div>
<div id="comment-30596-info" class="comment-info">
<span class="comment-age">(10 Feb '14, 19:34)</span> <span class="comment-user userinfo">SaleksV</span>
</div>
</div>
<span id="30597"></span>
<div id="comment-30597" class="comment">
<div id="post-30597-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>SaleksV, please give more information about what you are doing. How are you trying to extract the addresses in step 4? What are it's intended uses?</p>
</div>
<div id="comment-30597-info" class="comment-info">
<span class="comment-age">(10 Feb '14, 19:44)</span> <span class="comment-user userinfo">jgpacker</span>
</div>
</div>
<span id="30614"></span>
<div id="comment-30614" class="comment">
<div id="post-30614-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, I'm trying to export the map area to *.osm file. It does contain all the information I need. The problem is that "Export" allows to export only rectangular selection, which is not enough accurate. So the aim is have free polygon selection and then export it to osm, which contains the list of housenumbers and street names (addresses). The purpose of having this info is to assign some specific responsible person for exact map area (responsible for buildings maintenance, cleaning and so on). So having list of addresses will be more informative for this person.</p>
</div>
<div id="comment-30614-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 07:01)</span> <span class="comment-user userinfo">SaleksV</span>
</div>
</div>
<span id="30615"></span>
<div id="comment-30615" class="comment not_top_scorer">
<div id="post-30615-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Also it would be great to have the possibility to assign a name to free selection on map. So in future I'm able to assign another responsible person. Is there a possibility to store this area not in public, but for example in my account, so these stored areas do not interfere other public users. I hope I was able to describe the overall aim. I guess the steps I have described earlier should be more clear at the moment. Thank you!</p>
</div>
<div id="comment-30615-info" class="comment-info">
<span class="comment-age">(11 Feb '14, 07:07)</span> <span class="comment-user userinfo">SaleksV</span>
</div>
</div>
<span id="30681"></span>
<div id="comment-30681" class="comment">
<div id="post-30681-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ok, thanks for the clarification. <a href="https://wiki.openstreetmap.org/wiki/Creating_city_pages">You can create a wiki page to your city to do this kind of organized mapping</a>, maybe with a section to each user and/or place, with a link to each place(like <a href="http://osm.org/go/0pCq7JAwe">http://osm.org/go/0pCq7JAwe</a> ), and if the link is not accurate enough, you can list all those names there too(or just provide an explanation with it).</p>
<p>If this does not meet your needs, you should ask another question in this site asking for ways to "assign" areas to other users, so you can map colaboratively a place.</p>
</div>
<div id="comment-30681-info" class="comment-info">
<span class="comment-age">(12 Feb '14, 12:11)</span> <span class="comment-user userinfo">jgpacker</span>
</div>
</div>
</div>
<div id="comment-tools-30587" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-30587-form-container" class="comment-form-container">
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

<span id="30595"></span>

<div id="answer-container-30595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30595-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think what you are really looking for is the "<em>Where am I?</em>" link in <a href="http://www.openstreetmap.org/?locale=en">OpenStretMap</a>'s search box, or whatever is shown in your locale(with roughly the same meaning).</p>
<p>That link will give you the coordinate of the center point of your current view, and try to reverse geocode the address.</p>
<p>Alternatively, you can click into the <em>Layers</em> button and check the <em>Map Data</em> checkbox. This way you can click on the elements to see their attributes. If they have their address there, it will be shown. (if the object has a name, you can simply search for it).</p>
<p>EDIT:</p>
<p>Ok, thanks for the clarification. You can create a wiki page to your city to do this kind of organized mapping, maybe with a section to each user and/or place, with a link to each place(like <a href="http://osm.org/go/0pCq7JAwe">http://osm.org/go/0pCq7JAwe</a> ), and if the link is not accurate enough, you can list all those names there too(or just provide an explanation with it).</p>
<p>If this does not meet your needs, you should ask another question in this site asking for ways to "assign" areas to other users, so you can map colaboratively a place. PS: If your intention is to get the address with a software, show us the code you tried to use, the documentation you read, and whatever else you judge necessary.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Feb '14, 19:09</strong></p>
<img src="https://secure.gravatar.com/avatar/704f28429974bab1704a7535eb8a5734?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jgpacker&#39;s gravatar image" />
<p><span>jgpacker</span><br />
<span class="score" title="236 reputation points">236</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jgpacker has one accepted answer">10%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Feb '14, 15:27</strong> </span></p>
</div>
</div>
<div id="comments-container-30595" class="comments-container">
&#10;</div>
<div id="comment-tools-30595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30595-form-container" class="comment-form-container">
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

