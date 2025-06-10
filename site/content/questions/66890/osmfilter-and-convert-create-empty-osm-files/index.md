+++
type = "question"
title = "[closed] osmfilter and convert create empty osm files"
description = '''Hello My objective is to create a csv file of all the shops in graz located in the country of austria. Since I don&#x27;t have enough space to unzip the austria osm file so I used bzcat to unzip from the terminal. i used the graz.poly file to help me filter the shops in graz. this is how my command with ...'''
date = "2018-11-22T19:42:00Z"
lastmod = "2018-11-24T09:47:00Z"
weight = 66890
keywords = [ "osmconvert", "osmfilter", ".osm", "empty" ]
aliases = [ "/questions/66890" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] osmfilter and convert create empty osm files](/questions/66890/osmfilter-and-convert-create-empty-osm-files)

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
<span id="post-66890-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-66890-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-66890-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello My objective is to create a csv file of all the shops in graz located in the country of austria.</p>
<p>Since I don't have enough space to unzip the austria osm file so I used bzcat to unzip from the terminal.</p>
<p>i used the graz.poly file to help me filter the shops in graz.</p>
<p>this is how my command with pipes looks like.</p>
<p>bzcat 2018-austia-latest.osm.bz2 | osmconvert - -B=Graz.poly -o=mys.osm | ./osmfilter mys.osm --keep= --nodes="shops=" -o=graz_shops.osm | ./osmconvert graz_shops.osm --all-to-nodes --csv="<a href="https://help.openstreetmap.org/users/260/idoneus">@id</a> <a href="https://help.openstreetmap.org/users/1350/longestaugust">@lon</a> <a href="https://help.openstreetmap.org/users/5110/latroc">@lat</a> name" -o=grazshops.csv</p>
<p>however when i enter this in the terminal</p>
<p>I get osmfilter error: file empty: graz_shops.osm osmconvert error: file empty: mys.osm</p>
<p>can anyone tell me what I am doing wrong? thank you in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmconvert" rel="tag" title="see questions tagged &#39;osmconvert&#39;">osmconvert</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span> <span class="post-tag tag-link-.osm" rel="tag" title="see questions tagged &#39;.osm&#39;">.osm</span> <span class="post-tag tag-link-empty" rel="tag" title="see questions tagged &#39;empty&#39;">empty</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Nov '18, 19:42</strong></p>
<img src="https://secure.gravatar.com/avatar/b6bb34d9fa6aa58acfbe782f8aa06df4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="osmnoob&#39;s gravatar image" />
<p><span>osmnoob</span><br />
<span class="score" title="10 reputation points">10</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="osmnoob has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Nov '18, 11:58</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-66890" class="comments-container">
<span id="66897"></span>
<div id="comment-66897" class="comment">
<div id="post-66897-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Cross-posted on both the OSM Forum and the OSM subreddit. The forum provides answers: <a href="https://forum.openstreetmap.org/viewtopic.php?id=64569.">https://forum.openstreetmap.org/viewtopic.php?id=64569.</a></p>
<p><a href="https://help.openstreetmap.org/users/15943/osmnoob">@osmnoob</a>: cross-posting is generally regarded as a bad thing. People may expend time &amp; effort providing an answer to a question which has already been answered elsewhere. It is particularly annoying when you are asking others to do your course work for you. Please do not do this again on any online Q&amp;A system.</p>
</div>
<div id="comment-66897-info" class="comment-info">
<span class="comment-age">(24 Nov '18, 09:47)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-66890" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-66890-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Duplicate Question: already asked & answered on OSM Forum." by SK53 24 Nov '18, 09:48

</div>

</div>

</div>

