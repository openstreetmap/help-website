+++
type = "question"
title = "Trouble installing TagTransform plugin for Osmosis"
description = '''Hi all, I am trying to install the TagTransform plugin for Osmosis, after doing following I get an exception.  download and copy the tagtransform.jar into /lib/default create osmosis-plugins.conf under /config and added &quot;uk.co.randomjunk.osmosis.transform.TransformPlugin&quot;  Run osmosis with --tag-tra...'''
date = "2011-08-23T18:15:00Z"
lastmod = "2011-08-24T00:19:00Z"
weight = 7276
keywords = [ "osmosis" ]
aliases = [ "/questions/7276" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Trouble installing TagTransform plugin for Osmosis](/questions/7276/trouble-installing-tagtransform-plugin-for-osmosis)

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
<span id="post-7276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7276-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi all,</p>
<p>I am trying to install the TagTransform plugin for Osmosis, after doing following I get an exception.</p>
<ol>
<li>download and copy the tagtransform.jar into /lib/default</li>
<li>create osmosis-plugins.conf under /config and added "uk.co.randomjunk.osmosis.transform.TransformPlugin"</li>
<li>Run osmosis with --tag-transform</li>
</ol>
<p>I got an exception saying PluginLoader class def not found. I am running it on Windows.</p>
<p>Any idea?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>23 Aug '11, 18:15</strong></p>
<img src="https://secure.gravatar.com/avatar/00dcbece2b58b70630eede8b2aed6911?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yingqi%20Tang&#39;s gravatar image" />
<p><span>Yingqi Tang</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yingqi Tang has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7276" class="comments-container">
&#10;</div>
<div id="comment-tools-7276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7276-form-container" class="comment-form-container">
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

<span id="7280"></span>

<div id="answer-container-7280" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7280-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7280-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7280-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think the problem is that the tagtransform.jar linked from the wiki is built for an older version of Osmosis. So it is lacking some of the classes required by the current version.</p>
<p>You could follow the instructions for <a href="http://wiki.openstreetmap.org/wiki/Osmosis/TagTransform#Building_the_jar_yourself_.28.3E.3D0.37.29">Building the TagTransform jar yourself</a>, using the current version of Osmosis and the TagTransform source from SVN. This will probably require installing Apache Ant, I don't know how easy that is on Windows.</p>
<p>Or try this tagtransform.jar that I have built for Osmosis v0.38: <a href="http://osmalba.org/work/tagtransform.jar">http://osmalba.org/work/tagtransform.jar</a> Just download it, and put it in the lib/default directory. This works fine for me, using Osmosis v0.38 on Windows. Though I am no expert on this, I'm not sure if it will work for anyone else, or with different versions of Osmosis.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Aug '11, 00:19</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-7280" class="comments-container">
&#10;</div>
<div id="comment-tools-7280" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7280-form-container" class="comment-form-container">
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

