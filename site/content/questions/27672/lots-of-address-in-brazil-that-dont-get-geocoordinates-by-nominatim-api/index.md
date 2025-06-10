+++
type = "question"
title = "lots of address in brazil that dont get geocoordinates by nominatim API"
description = '''Hi All, I am using openstreetmap api for fetching latitude and longitude values by providing address to the api. I am using below format of API:  http://nominatim.openstreetmap.org/search?street=229 Dr Brasilio Machado&amp;amp;city=São Paulo&amp;amp;country=Brasil&amp;amp;postalcode=01230-010&amp;amp;format=json&amp;am...'''
date = "2013-10-31T09:31:00Z"
lastmod = "2013-11-01T08:02:00Z"
weight = 27672
keywords = [ "nominatim", "geocoding" ]
aliases = [ "/questions/27672" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [lots of address in brazil that dont get geocoordinates by nominatim API](/questions/27672/lots-of-address-in-brazil-that-dont-get-geocoordinates-by-nominatim-api)

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
<span id="post-27672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27672-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi All,</p>
<p>I am using openstreetmap api for fetching latitude and longitude values by providing address to the api. I am using below format of API:<br />
</p>
<pre><code>http://nominatim.openstreetmap.org/search?street=229 Dr Brasilio Machado&amp;city=São Paulo&amp;country=Brasil&amp;postalcode=01230-010&amp;format=json&amp;polygon=1&amp;addressdetails=1</code></pre>
<p>I am getting values for most of the addresses all around the world. But For some addresses like one mentioned in the link i dont get lat/lon values.</p>
<p>Initially i was using the below format of Api.<br />
</p>
<pre><code>http://nominatim.openstreetmap.org/search?q=114, r. Voluntários da Pátria, Rio de Janeiro (Capital),cel 6929. 8703&amp;format=json</code></pre>
<p>But it was also have issue with some of the addresses so i switch to this format of API.</p>
<p>Can someone please help which is the best way to get lat/lon values for all addresses using openstreetmap?</p>
<p>Thanks</p>
<p>Umesh Tayade</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Oct '13, 09:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ebcbb78e817bbc20333945490fa28c39?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Umesh%20Tayade&#39;s gravatar image" />
<p><span>Umesh Tayade</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Umesh Tayade has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Oct '13, 11:49</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-27672" class="comments-container">
&#10;</div>
<div id="comment-tools-27672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27672-form-container" class="comment-form-container">
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

<span id="27673"></span>

<div id="answer-container-27673" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27673-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27673-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-27673-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can't get something out of the database that wasn't in there to start with. Unfortunately, the maps for anything except the core of the larger metropolitan regions in Brazil are very poor, and the thing that is lacking the most are the street names. It has shown some improvement in the last year, but still very poor. I contribute data solely inside Brazil (mostly São Paulo) and I find that most small cities outside São Paulo/Rio de Janeiro have nothing but the street traced, if even this.</p>
<p>For the street numbering, the situation cannot be described as anything but "terrible". For ZIP/Postal Codes, the same.</p>
<p>Some tips:</p>
<ul>
<li>Leave out the postal code in your queries. Based on your example query, I found that it is not found and restricts even more the already poor results.</li>
<li>Try experimenting with removing or using the full name qualifier. Ex.: Rua/R. for streets, Avenida/Av., for Avenues, and so on</li>
<li>Try experimenting with removing or using the full title qualifier. Ex.: Doutor/Dr. for "Doctor", Pres./Presidente for "President", and so on.</li>
<li>It doesn't matter if the street numbers are before or after the address, but since brazilian addresses are mostly written in the brazilian way (in the database), it <em>may help</em> to query them in this way.</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Oct '13, 11:42</strong></p>
<img src="https://secure.gravatar.com/avatar/94b019f273c04cd88bc1c8dd0a8f2161?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MCPicoli&#39;s gravatar image" />
<p><span>MCPicoli</span><br />
<span class="score" title="2172 reputation points"><span>2.2k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="MCPicoli has 10 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-27673" class="comments-container">
<span id="27688"></span>
<div id="comment-27688" class="comment">
<div id="post-27688-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Slightly OT: thanks to MCPicoli to working on adding data in Brazil. I think it it s important to realize that building a geodatabase/map of the whole world takes time and that we are doing this a lot faster than our competitors did, even our flagship regions took years to get to the state they are now in. As MCPicoli points out, in the days of widely available areial imagery getting road geometry is relatively cheap, but doesn't replace the need to have and build local communities that add the meta data (street names etc) that make the geometry data so much more useful.</p>
</div>
<div id="comment-27688-info" class="comment-info">
<span class="comment-age">(01 Nov '13, 08:02)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-27673" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27673-form-container" class="comment-form-container">
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

