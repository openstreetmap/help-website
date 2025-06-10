+++
type = "question"
title = "Finding all new elements from a user"
description = '''Hi,  I am struggling with attempting to find all brand new elements created by a single user. I have currently the following but how do I check for version=1 (or similar) please so I only get where they have created a brand new element please? Happy with any other alternatives. What I would like to ...'''
date = "2018-05-05T10:34:00Z"
lastmod = "2018-05-06T16:16:00Z"
weight = 63321
keywords = [ "version", "user" ]
aliases = [ "/questions/63321" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Finding all new elements from a user](/questions/63321/finding-all-new-elements-from-a-user)

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
<span id="post-63321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63321-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-63321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am struggling with attempting to find all brand new elements created by a single user. I have currently the following but how do I check for version=1 (or similar) please so I only get where they have created a brand new element please? Happy with any other alternatives. What I would like to validate new work by a particular user where they have created a road or similar. I am not interested in their modifications to existing content.</p>
<p>Thanks</p>
<pre><code>{{user=funkyUserName}}
&lt;osm-script output=&quot;json&quot;&gt;
  &lt;union&gt;
    &lt;query type=&quot;node&quot;&gt;
       &lt;user name=&quot;{{user}}&quot;/&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
    &lt;query type=&quot;way&quot;&gt;
      &lt;user name=&quot;{{user}}&quot;  /&gt;
      &lt;bbox-query {{bbox}}/&gt;
    &lt;/query&gt;
  &lt;/union&gt;
  &lt;print mode=&quot;body&quot;/&gt;
  &lt;recurse type=&quot;down&quot;/&gt;
  &lt;print mode=&quot;skeleton&quot;/&gt;
&lt;/osm-script&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-version" rel="tag" title="see questions tagged &#39;version&#39;">version</span> <span class="post-tag tag-link-user" rel="tag" title="see questions tagged &#39;user&#39;">user</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>05 May '18, 10:34</strong></p>
<img src="https://secure.gravatar.com/avatar/a8dbda930e9da736915267cbe67e5f05?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Ewen%20Hill&#39;s gravatar image" />
<p><span>Ewen Hill</span><br />
<span class="score" title="91 reputation points">91</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Ewen Hill has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 May '18, 02:28</strong> </span></p>
</div>
</div>
<div id="comments-container-63321" class="comments-container">
&#10;</div>
<div id="comment-tools-63321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-63321-form-container" class="comment-form-container">
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

<span id="63329"></span>

<div id="answer-container-63329" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-63329-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-63329-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-63329-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Ewen Hill has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Depending on the size of the area the user has edited in, I'll recommend just loading it in JOSM, then run the search (Ctrl-F) <strong>user:spjaquish version:1</strong></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '18, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/6edf3a421a450237beae62ba93582637?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hjart&#39;s gravatar image" />
<p><span>Hjart</span><br />
<span class="score" title="2961 reputation points"><span>3.0k</span></span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="26 badges"><span class="silver">●</span><span class="badgecount">26</span></span><span title="56 badges"><span class="bronze">●</span><span class="badgecount">56</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hjart has 14 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>05 May '18, 18:53</strong> </span></p>
</div>
</div>
<div id="comments-container-63329" class="comments-container">
<span id="63332"></span>
<div id="comment-63332" class="comment not_top_scorer">
<div id="post-63332-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, this is excellent but the area is huge so an Overpass method would still be wonderful</p>
</div>
<div id="comment-63332-info" class="comment-info">
<span class="comment-age">(05 May '18, 21:28)</span> <span class="comment-user userinfo">Ewen Hill</span>
</div>
</div>
<span id="63333"></span>
<div id="comment-63333" class="comment">
<div id="post-63333-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Ok. Overpass queries can be run from within JOSM. In the Download window, select the "download from Overpass" tab, click the wizard button and enter 'user:spjaquish', then on the map select the bbox to search within, then press download. When data is downloaded, do Ctrl-F 'version:1'</p>
<p>See <a href="https://josm.openstreetmap.de/wiki/Help/Action/Download">https://josm.openstreetmap.de/wiki/Help/Action/Download</a></p>
</div>
<div id="comment-63333-info" class="comment-info">
<span class="comment-age">(05 May '18, 21:37)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="63336"></span>
<div id="comment-63336" class="comment">
<div id="post-63336-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Just for completeness, here's an example of restricting a query to version=1 objects: <a href="http://overpass-turbo.eu/s/yyr">http://overpass-turbo.eu/s/yyr</a> .</p>
<p>Not sure how the performance would be.</p>
</div>
<div id="comment-63336-info" class="comment-info">
<span class="comment-age">(05 May '18, 23:42)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="63338"></span>
<div id="comment-63338" class="comment not_top_scorer">
<div id="post-63338-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you <a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a> and <a href="https://help.openstreetmap.org/users/3577/hjart">@Hjart</a> as both of you have been a wealth of knowledge. The Overpass example did the trick but I was also unaware of the JOSM options. Performance is dire as we are looking at 4000km by 3000km area however I expected this.</p>
</div>
<div id="comment-63338-info" class="comment-info">
<span class="comment-age">(06 May '18, 02:34)</span> <span class="comment-user userinfo">Ewen Hill</span>
</div>
</div>
<span id="63340"></span>
<div id="comment-63340" class="comment">
<div id="post-63340-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I almost always prefer the JOSM option, because it allows closer inspection without having to go through further hoops. <a href="https://wiki.openstreetmap.org/wiki/JOSM/Plugins/TODO_list">https://wiki.openstreetmap.org/wiki/JOSM/Plugins/TODO_list</a> also often comes in extremely handy.</p>
<p>Also note that simpler Overpass queries of course always perform better.</p>
</div>
<div id="comment-63340-info" class="comment-info">
<span class="comment-age">(06 May '18, 08:02)</span> <span class="comment-user userinfo">Hjart</span>
</div>
</div>
<span id="63343"></span>
<div id="comment-63343" class="comment">
<div id="post-63343-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10973/maxerickson">@maxerickson</a>, Wonderful answer. But is there any way to accomplish the same thing using only the Overpass Turbo Wizard? I don't want to have to learn the complex syntax of the standard Query Language.</p>
</div>
<div id="comment-63343-info" class="comment-info">
<span class="comment-age">(06 May '18, 15:47)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="63346"></span>
<div id="comment-63346" class="comment">
<div id="post-63346-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I guess not. Wizard features should be documented on <a href="https://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard">https://wiki.openstreetmap.org/wiki/Overpass_turbo/Wizard</a> fairly soon after they exist. It seems it could support something like version:1, but it does not right now.</p>
</div>
<div id="comment-63346-info" class="comment-info">
<span class="comment-age">(06 May '18, 16:16)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
</div>
<div id="comment-tools-63329" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-63329-form-container" class="comment-form-container">
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

