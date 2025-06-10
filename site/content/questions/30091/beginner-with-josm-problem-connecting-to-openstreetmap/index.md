+++
type = "question"
title = "Beginner with JOSM - problem connecting to OpenStreetMap"
description = '''I am trying to download a relation and all of its members in JOSM. The relation 161648 (admin_level = 4) (Nebraska boundary). I am trying to make sure that the relation members are sorted and I understand I can do that in JOSM. When I go to download object, It looks like it tries to make a connectio...'''
date = "2014-01-22T15:36:00Z"
lastmod = "2014-01-22T19:31:00Z"
weight = 30091
keywords = [ "josm", "connection", "failed" ]
aliases = [ "/questions/30091" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Beginner with JOSM - problem connecting to OpenStreetMap](/questions/30091/beginner-with-josm-problem-connecting-to-openstreetmap)

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
<span id="post-30091-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30091-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-30091-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to download a relation and all of its members in JOSM. The relation 161648 (admin_level = 4) (Nebraska boundary). I am trying to make sure that the relation members are sorted and I understand I can do that in JOSM. When I go to download object, It looks like it tries to make a connection to OpenStreetMap API and it fails. It comes back with no data. I have enabled remote control in JOSM. Also when I push the edit in OpenStreetMap, JOSM start to make a connection and comes back with the message "Failed to open a connection to the remote server <a href="http://api.openstreet.org/api/">http://api.openstreet.org/api/"</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-connection" rel="tag" title="see questions tagged &#39;connection&#39;">connection</span> <span class="post-tag tag-link-failed" rel="tag" title="see questions tagged &#39;failed&#39;">failed</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Jan '14, 15:36</strong></p>
<img src="https://secure.gravatar.com/avatar/343237842fce1f7a82f69ebf7a92f6b6?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kcjailbirds&#39;s gravatar image" />
<p><span>kcjailbirds</span><br />
<span class="score" title="141 reputation points">141</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kcjailbirds has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Mar '19, 10:44</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/ba4d3e91f235ed21dacc1766b94e26a8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richlv&#39;s gravatar image" />
<p><span>Richlv</span><br />
<span class="score" title="1740 reputation points"><span>1.7k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="31 badges"><span class="silver">●</span><span class="badgecount">31</span></span><span title="42 badges"><span class="bronze">●</span><span class="badgecount">42</span></span></p>
</div>
</div>
<div id="comments-container-30091" class="comments-container">
<span id="30099"></span>
<div id="comment-30099" class="comment">
<div id="post-30099-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Side question: why would you want to sort admin boundary members?</p>
</div>
<div id="comment-30099-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:30)</span> <span class="comment-user userinfo">RM87</span>
</div>
</div>
<span id="30101"></span>
<div id="comment-30101" class="comment">
<div id="post-30101-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am trying to create a SQLGeography object from the admin boundary using C# and it cannot. I believe it results in illegal polygons due to sorting issues. At least that is my guess.</p>
</div>
<div id="comment-30101-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:44)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="30102"></span>
<div id="comment-30102" class="comment">
<div id="post-30102-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Couldn't you sort the relation in the client program? It'll only get unsorted again when someone updates the relation in OSM.</p>
</div>
<div id="comment-30102-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="30105"></span>
<div id="comment-30105" class="comment">
<div id="post-30105-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure how to do that.</p>
</div>
<div id="comment-30105-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:54)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="30107"></span>
<div id="comment-30107" class="comment not_top_scorer">
<div id="post-30107-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If your sorting fixes an actual problem in the relation (such as making sure that the ways form a continuous ring with no gap) then go ahead and fix the data. If it is some problem related to your software (for example requiring outer rings before inner ones), then fix your software instead.</p>
</div>
<div id="comment-30107-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 17:02)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="30111"></span>
<div id="comment-30111" class="comment">
<div id="post-30111-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>...And checking the relation in question, it looks fine. No sorting required. Go fix your software :)</p>
</div>
<div id="comment-30111-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 17:08)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="30113"></span>
<div id="comment-30113" class="comment not_top_scorer">
<div id="post-30113-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Vincent! The same software works well with other states in US that I have tried so far. Neighboring states to Nebraska like Missouri, Iowa, and Kansas all work well but not Nebraska. How did you check the relation in question and noticed no sorting was required?</p>
</div>
<div id="comment-30113-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 17:30)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="30117"></span>
<div id="comment-30117" class="comment not_top_scorer">
<div id="post-30117-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Checked the relation by opening it in josm and seeing that it constitute a single well-ordered ring.</p>
</div>
<div id="comment-30117-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 19:31)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30091" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-30091-form-container" class="comment-form-container">
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

<span id="30100"></span>

<div id="answer-container-30100" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30100-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30100-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-30100-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A few suggestions :</p>
<ul>
<li>The hostname has a typo in your question. Try going into josm "preferences -&gt; connection settings" and check "use the default osm server url".</li>
<li>Can you download <a href="http://api.openstreetmap.org/api/0.6/relation/161648">http://api.openstreetmap.org/api/0.6/relation/161648</a> using a web browser like firefox ? If not, there is some kind of network problem that isn't JOSM's fault.</li>
<li>Check your josm proxy setting by going to "preferences -&gt; connection settings -&gt; proxy settings" if you connect to the internet via a proxy (copy the config from your internet browser).</li>
<li>It's probably not the problem, but make sure that you are using a recent version of josm (6502 is the current stable).</li>
</ul>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Jan '14, 16:35</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Jan '14, 19:39</strong> </span></p>
</div>
</div>
<div id="comments-container-30100" class="comments-container">
<span id="30103"></span>
<div id="comment-30103" class="comment">
<div id="post-30103-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>sorry, it actually says "faile to open connection to the remote server <a href="http://api.openstreetmap.org/api.">http://api.openstreetmap.org/api.</a> I am trying to download it from JOSM so that I can attempt to sort the members.</p>
</div>
<div id="comment-30103-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:50)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="30104"></span>
<div id="comment-30104" class="comment">
<div id="post-30104-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I am also using version 6502 of JOSM.</p>
</div>
<div id="comment-30104-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 16:50)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="30110"></span>
<div id="comment-30110" class="comment">
<div id="post-30110-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, what about the 2nd suggestion (downloading using a browser to test for non-josm problems) ?</p>
</div>
<div id="comment-30110-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 17:04)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="30112"></span>
<div id="comment-30112" class="comment">
<div id="post-30112-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I did download the relation using the browser. That only gave me the ways forming the relation and not the nodes. Is their a way to get a download of the ways and nodes that form the relation and ways?</p>
</div>
<div id="comment-30112-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 17:27)</span> <span class="comment-user userinfo">kcjailbirds</span>
</div>
</div>
<span id="30114"></span>
<div id="comment-30114" class="comment">
<div id="post-30114-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Are you behind a proxy ? You need to configure the proxy in JOSM</p>
</div>
<div id="comment-30114-info" class="comment-info">
<span class="comment-age">(22 Jan '14, 17:37)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-30100" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30100-form-container" class="comment-form-container">
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

