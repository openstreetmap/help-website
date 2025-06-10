+++
type = "question"
title = "How to get tile request log file?"
description = '''In the log file server, there is summarized version of count for all requested tiles(http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/network_in.html ). But I need how many time tile being requested for each tile for the result like this(http://datamining.typepad.com/data_mining/2007/...'''
date = "2014-03-07T06:23:00Z"
lastmod = "2014-03-07T11:11:00Z"
weight = 31378
keywords = [ "tiles" ]
aliases = [ "/questions/31378" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to get tile request log file?](/questions/31378/how-to-get-tile-request-log-file)

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
<span id="post-31378-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31378-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31378-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In the log file server, there is summarized version of count for all requested tiles(<a href="http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/network_in.html">http://munin.openstreetmap.org/openstreetmap/tile.openstreetmap/network_in.html</a> ).</p>
<p>But I need how many time tile being requested for each tile for the result like this(<a href="http://datamining.typepad.com/data_mining/2007/04/mapping_mapping.html)">http://datamining.typepad.com/data_mining/2007/04/mapping_mapping.html)</a></p>
<p>Does anybody know how can I access or acquire for each tile log. In the server, there should be an apache file log for each HTTP GET request such as 2014 08 07 hour min second ..... <a href="http://tile.openstreetmap.com/z/y/x.png">http://tile.openstreetmap.com/z/y/x.png</a> GET.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>07 Mar '14, 06:23</strong></p>
<img src="https://secure.gravatar.com/avatar/46ad573fc66aab48f609aa683b84735b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="wongeun&#39;s gravatar image" />
<p><span>wongeun</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="wongeun has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>07 Mar '14, 06:33</strong> </span></p>
</div>
</div>
<div id="comments-container-31378" class="comments-container">
<span id="31381"></span>
<div id="comment-31381" class="comment">
<div id="post-31381-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Can you explain <em>why</em> you want access to the raw logs rather than the collated stats that are already available?</p>
</div>
<div id="comment-31381-info" class="comment-info">
<span class="comment-age">(07 Mar '14, 10:10)</span> <span class="comment-user userinfo">Jonathan Ben...</span>
</div>
</div>
<span id="31382"></span>
<div id="comment-31382" class="comment">
<div id="post-31382-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I just know my this summary on clients but thats not related to single tiles:<br />
<a href="http://www.openstreetmap.org/user/!i!/diary/15190">http://www.openstreetmap.org/user/!i!/diary/15190</a></p>
<p>OSM now has multiple tiles servers and makes use of geoip to work as mini CDN, so I guess it's pretty hard to aggregate this data (and keep the privacy)</p>
</div>
<div id="comment-31382-info" class="comment-info">
<span class="comment-age">(07 Mar '14, 11:04)</span> <span class="comment-user userinfo">iii</span>
</div>
</div>
</div>
<div id="comment-tools-31378" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31378-form-container" class="comment-form-container">
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

<span id="31384"></span>

<div id="answer-container-31384" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31384-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31384-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-31384-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Web server logs are not published by OSM(F).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Mar '14, 11:11</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span> </br></p>
</div>
</div>
<div id="comments-container-31384" class="comments-container">
&#10;</div>
<div id="comment-tools-31384" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31384-form-container" class="comment-form-container">
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

