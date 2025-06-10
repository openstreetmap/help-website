+++
type = "question"
title = "Process diffs with extra table"
description = '''I have splitted off the places from the osm_point table and I&#x27;m wondering how the processing of diff files is going to work. In my testsetup I have this for the points:  function osm2pgsql.process_node(object)  if clean_tags(object.tags) then  return  end local place = object.tags.place if place == ...'''
date = "2021-09-06T13:05:00Z"
lastmod = "2021-09-07T08:01:00Z"
weight = 81635
keywords = [ "osm2pgsql" ]
aliases = [ "/questions/81635" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Process diffs with extra table](/questions/81635/process-diffs-with-extra-table)

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
<span id="post-81635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have splitted off the places from the osm_point table and I'm wondering how the processing of diff files is going to work.</p>
<p>In my testsetup I have this for the points: function osm2pgsql.process_node(object) if clean_tags(object.tags) then return end</p>
<pre><code>local place = object.tags.place
if place == &#39;city&#39; or place == &#39;town&#39; or place == &#39;village&#39; or place == &#39;hamlet&#39; or place == &#39;borough&#39; or place == &#39;suburb&#39; or place == &#39;quarter&#39; or place == &#39;neighbourhood&#39; then
  tables.place:add_row({ tags = object.tags })
else
  tables.point:add_row({ tags = object.tags })
end</code></pre>
<p>end</p>
<p>so places end up in the place table and <em>not</em> in the points. If diffs are processed, will that work correctly? So f.e. if the place-tag is deleted from a point, will it be deleted from my place table and inserted into the point table? (I mean: the add_row() implies that only additions will be done through the process_node function...)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm2pgsql" rel="tag" title="see questions tagged &#39;osm2pgsql&#39;">osm2pgsql</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Sep '21, 13:05</strong></p>
<img src="https://secure.gravatar.com/avatar/31d950f81ca152c66d5ed83bb7c53950?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Paulosm2016&#39;s gravatar image" />
<p><span>Paulosm2016</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Paulosm2016 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-81635" class="comments-container">
&#10;</div>
<div id="comment-tools-81635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81635-form-container" class="comment-form-container">
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

<span id="81662"></span>

<div id="answer-container-81662" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-81662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-81662-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-81662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, this will all work magically. You don't have to think about this, osm2pgsql will just handle it for you correctly. Just write your config file like there were no updated at all.</p>
<p>Internally what happens is that all entries in all tables derived from changed objects will be deleted and, possibly, re-added based on whats in your config file. (This is certainly not the most efficient way to do this, but the easiest. It might be handled differently in the future, so you should not rely on the details of this mechanism.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>07 Sep '21, 08:01</strong></p>
<img src="https://secure.gravatar.com/avatar/2d4dfcdcde73aa5e2ffa4a9b3a7cb51d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jochen%20Topf&#39;s gravatar image" />
<p><span>Jochen Topf</span><br />
<span class="score" title="5244 reputation points"><span>5.2k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="50 badges"><span class="silver">●</span><span class="badgecount">50</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jochen Topf has 32 accepted answers">31%</span></p>
</div>
</div>
<div id="comments-container-81662" class="comments-container">
&#10;</div>
<div id="comment-tools-81662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-81662-form-container" class="comment-form-container">
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

