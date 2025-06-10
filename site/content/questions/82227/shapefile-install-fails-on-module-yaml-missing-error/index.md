+++
type = "question"
title = "shapefile install fails on module yaml missing error"
description = '''Hello, I try to setup a tile server with this tutorial: https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/. The process can not be continued at SHAPEFILE DOWNLOAD, because module YAML is missing. I´m not familiar with python, what can I do? Error hits here: scripts/get-e...'''
date = "2021-10-19T00:20:00Z"
lastmod = "2021-10-19T10:07:00Z"
weight = 82227
keywords = [ "python", "shapefile", "tileserver" ]
aliases = [ "/questions/82227" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [shapefile install fails on module yaml missing error](/questions/82227/shapefile-install-fails-on-module-yaml-missing-error)

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
<span id="post-82227-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82227-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82227-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I try to setup a tile server with this tutorial: <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/.">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/.</a> The process can not be continued at SHAPEFILE DOWNLOAD, because module YAML is missing. I´m not familiar with python, what can I do? Error hits here:</p>
<pre><code>scripts/get-external-data.py</code></pre>
<p>Thx and Regards</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-python" rel="tag" title="see questions tagged &#39;python&#39;">python</span> <span class="post-tag tag-link-shapefile" rel="tag" title="see questions tagged &#39;shapefile&#39;">shapefile</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Oct '21, 00:20</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee56dffff70eb5c464e336817ac08a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dom771013&#39;s gravatar image" />
<p><span>Dom771013</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dom771013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82227" class="comments-container">
<span id="82236"></span>
<div id="comment-82236" class="comment">
<div id="post-82236-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Could you provide a full output of the error?</p>
</div>
<div id="comment-82236-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 08:24)</span> <span class="comment-user userinfo">Marcos Dione</span>
</div>
</div>
</div>
<div id="comment-tools-82227" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82227-form-container" class="comment-form-container">
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

<span id="82235"></span>

<div id="answer-container-82235" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82235-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82235-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-82235-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be able to install a system wide version with <code>sudo apt install python3-yaml</code>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 08:23</strong></p>
<img src="https://secure.gravatar.com/avatar/e4587465b2b1b94834e5e625b80a29dd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Marcos%20Dione&#39;s gravatar image" />
<p><span>Marcos Dione</span><br />
<span class="score" title="71 reputation points">71</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Marcos Dione has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82235" class="comments-container">
<span id="82237"></span>
<div id="comment-82237" class="comment">
<div id="post-82237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've updated <a href="https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/">https://switch2osm.org/serving-tiles/manually-building-a-tile-server-20-04-lts/</a> to include python3-yaml . It was present in the Debian 11 guide but not the Ubuntu 20.04 one.</p>
<p>What software is needed changed as what's packaged in various OSes, and also in things like OSM Carto itself, change ver time.</p>
</div>
<div id="comment-82237-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 09:29)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82235" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82235-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82234"></span>

<div id="answer-container-82234" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82234-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82234-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82234-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I also tried to install YAML by: /usr/bin/python -m pip install pyyaml</p>
<p>I found that here (last post): <a href="https://github.com/yaml/pyyaml/issues/291">https://github.com/yaml/pyyaml/issues/291</a></p>
<p>So PIP seems also not beeing installed. What went wrong? I missed no line of the tutorial.</p>
<p>Regards</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 07:24</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee56dffff70eb5c464e336817ac08a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dom771013&#39;s gravatar image" />
<p><span>Dom771013</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dom771013 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82234" class="comments-container">
<span id="82238"></span>
<div id="comment-82238" class="comment">
<div id="post-82238-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<blockquote>
<p>I missed no line of the tutorial.</p>
</blockquote>
<p>No, you didn't. A dependency (that wasn't previously needed but now is) was missing. I've added it at <a href="https://github.com/switch2osm/switch2osm.github.io/pull/170">https://github.com/switch2osm/switch2osm.github.io/pull/170</a> .</p>
<p>The switch2osm guides use the package manager in your OS where possible, in this case Ubuntu's "apt". These days every 2-bit language has at least one package manager (python has "pip" and "cpan", node.js has "npm" and "yarn"). These guides don't use those but instead uses packages bundled (and tested) by Ubuntu.</p>
</div>
<div id="comment-82238-info" class="comment-info">
<span class="comment-age">(19 Oct '21, 09:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82234" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82234-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82241"></span>

<div id="answer-container-82241" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82241-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82241-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-82241-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I solved this my manually adding pip3 and after that by additionally install of pyyaml and requests. The card works now as expected. Thx</p>
<pre><code>sudo apt install python3-pip
/usr/bin/python3 -m pip install pyyaml
/usr/bin/python3 -m pip install requests
/usr/bin/python3 -c &#39;import yaml&#39;</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Oct '21, 10:07</strong></p>
<img src="https://secure.gravatar.com/avatar/2ee56dffff70eb5c464e336817ac08a5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Dom771013&#39;s gravatar image" />
<p><span>Dom771013</span><br />
<span class="score" title="61 reputation points">61</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Dom771013 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '21, 10:12</strong> </span></p>
</div>
</div>
<div id="comments-container-82241" class="comments-container">
&#10;</div>
<div id="comment-tools-82241" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82241-form-container" class="comment-form-container">
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

