+++
type = "question"
title = "Performance: virtual vs. non-virtual machine"
description = '''Dear all, For a project I&#x27;ve started to set up an own instance of the OSM infrastructure. For now I&#x27;ve started to use the vagrant-machine, so I haven&#x27;t installed the OSM-website directly on my machine. Unfortunately the performance in the vagrant-instance is not that good as I&#x27;ve hoped. Of course I ...'''
date = "2014-05-14T18:49:00Z"
lastmod = "2014-05-16T17:06:00Z"
weight = 33180
keywords = [ "performance", "osm" ]
aliases = [ "/questions/33180" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Performance: virtual vs. non-virtual machine](/questions/33180/performance-virtual-vs-non-virtual-machine)

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
<span id="post-33180-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33180-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33180-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Dear all,<br />
For a project I've started to set up an own instance of the OSM infrastructure. For now I've started to use the <a href="https://github.com/openstreetmap/openstreetmap-website/blob/master/VAGRANT.md">vagrant-machine</a>, so I haven't installed the OSM-website directly on my machine. Unfortunately the performance in the vagrant-instance is not that good as I've hoped. Of course I know that using a virtual machine is not that good, but I've assumed that it is a little bit faster.<br />
One exmaple:<br />
By browsing using the vagrant host from a blank website to the vagrant-osm-instance, the map view using takes about 27 seconds until the map appears.<br />
Is this only caused by the fact that I am using the vagrant machine? At least by checking the performance monitor it seems, that there is enough system capacities and that the system does not run at 100% load.<br />
</p>
<p>System: Intel Q6600: 4x3Ghz, 4GB DDR2, 500GB 7200rpm HD - not the best, but as already said: Only for development.</p>
<p>Would be nice to get some feedback :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-performance" rel="tag" title="see questions tagged &#39;performance&#39;">performance</span> <span class="post-tag tag-link-osm" rel="tag" title="see questions tagged &#39;osm&#39;">osm</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 May '14, 18:49</strong></p>
<img src="https://secure.gravatar.com/avatar/6fc6f0ce6b15926034073d61c76482fa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="schlomm&#39;s gravatar image" />
<p><span>schlomm</span><br />
<span class="score" title="56 reputation points">56</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="schlomm has no accepted answers">0%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33180" class="comments-container">
&#10;</div>
<div id="comment-tools-33180" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33180-form-container" class="comment-form-container">
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

<span id="33245"></span>

<div id="answer-container-33245" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33245-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33245-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33245-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The "map appearing" is not really very much related to the perfomance of the rails port on your system, since</p>
<p>a) most of the computations are done in JS in the leaflet library</p>
<p>b) you are not rendering tiles locally, but are using the normal OSM tile servers</p>
<p>assuming that the machine you have your browser installed on is not the virtual machine. If you -are- running the browser on the VM, that is likely your problem.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 May '14, 17:06</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span> </br></br></p>
</div>
</div>
<div id="comments-container-33245" class="comments-container">
&#10;</div>
<div id="comment-tools-33245" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33245-form-container" class="comment-form-container">
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

