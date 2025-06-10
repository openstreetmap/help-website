+++
type = "question"
title = "No valid (active) renderd config section available"
description = '''Hi,  I’m trying to set up a tile server following the instructions at - switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/ I have a fresh install of Ubuntu Linux 20.04 LTS. I’m ok as far as the Apache2 Ubuntu Default Page but when I try to run renderd for the first time with- $ ...'''
date = "2021-08-02T09:27:00Z"
lastmod = "2021-08-02T16:36:00Z"
weight = 81161
keywords = [ "renderd.conf", "renderd", "config", "tileserver" ]
aliases = [ "/questions/81161" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [No valid (active) renderd config section available](/questions/81161/no-valid-active-renderd-config-section-available)

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
<span id="post-81161-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81161-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81161-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I’m trying to set up a tile server following the instructions at - switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</p>
<p>I have a fresh install of Ubuntu Linux 20.04 LTS.</p>
<p>I’m ok as far as the Apache2 Ubuntu Default Page but when I try to run renderd for the first time with- $ renderd -f -c /usr/local/etc/renderd.conf I get the following-</p>
<p>renderd[150270]: Rendering daemon started</p>
<p>renderd[150270]: Initiating request_queue</p>
<p>renderd[150270]: Parsing section mapnik</p>
<p>renderd[150270]: Parsing section ajt</p>
<p>No valid (active) renderd config section available</p>
<p>As per the instruction I have edited renderd.conf so the first line is;-</p>
<pre><code>XML=/home/fozz/src/openstreetmap-carto/mapnik.xml[renderd]</code></pre>
<p>And the file mapnik.xml is at that location and consists of 4k+ lines. I’m not sure where to go next, any help will be greatly appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-renderd.conf" rel="tag" title="see questions tagged &#39;renderd.conf&#39;">renderd.conf</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-config" rel="tag" title="see questions tagged &#39;config&#39;">config</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Aug '21, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/a8627f1419d1554fe171aecb4537db5f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="chris&#39;s gravatar image" />
<p><span>chris</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="chris has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Aug '21, 16:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-81161" class="comments-container">
&#10;</div>
<div id="comment-tools-81161" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81161-form-container" class="comment-form-container">
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

<span id="81171"></span>

<div id="answer-container-81171" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81171-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81171-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81171-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the first line really is "XML=/home/fozz/src/openstreetmap-carto/mapnik.xml[renderd]" then it looks like you've just added something at the very beginning of the file. You can see a working one <a href="https://github.com/SomeoneElseOSM/mod_tile/blob/switch2osm/renderd.conf">here</a>.</p>
<p>In there, in the "ajt" section there is the line "XML=/home/renderaccount/src/openstreetmap-carto/mapnik.xml". If you're using the named map style "ajt" then you'll need to update the "XML" setting under "[ajt]" to point to "/home/fozz/src/openstreetmap-carto/mapnik.xml".</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Aug '21, 16:36</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-81171" class="comments-container">
&#10;</div>
<div id="comment-tools-81171" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81171-form-container" class="comment-form-container">
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

