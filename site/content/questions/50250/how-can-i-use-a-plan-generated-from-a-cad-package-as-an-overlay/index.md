+++
type = "question"
title = "How can I use a plan generated from a CAD package as an overlay?"
description = '''I have generated a plan from my own ground survey. I would like to use this as an accurate overlay when editing OSM. The ground survey has been plotted in QCAD pro which can export files in bmp,svg,pdf and uses dxf or dwg format to natively save data.'''
date = "2016-06-16T17:59:00Z"
lastmod = "2016-06-18T21:26:00Z"
weight = 50250
keywords = [ "import", "editing", "ground", "survey", "overlay" ]
aliases = [ "/questions/50250" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How can I use a plan generated from a CAD package as an overlay?](/questions/50250/how-can-i-use-a-plan-generated-from-a-cad-package-as-an-overlay)

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
<span id="post-50250-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50250-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50250-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have generated a plan from my own ground survey. I would like to use this as an accurate overlay when editing OSM. The ground survey has been plotted in QCAD pro which can export files in bmp,svg,pdf and uses dxf or dwg format to natively save data.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-ground" rel="tag" title="see questions tagged &#39;ground&#39;">ground</span> <span class="post-tag tag-link-survey" rel="tag" title="see questions tagged &#39;survey&#39;">survey</span> <span class="post-tag tag-link-overlay" rel="tag" title="see questions tagged &#39;overlay&#39;">overlay</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jun '16, 17:59</strong></p>
<img src="https://secure.gravatar.com/avatar/2ef546bdea56f93f4203f7b581a6c6b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwallum&#39;s gravatar image" />
<p><span>bwallum</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwallum has one accepted answer">100%</span></p>
</div>
</div>
<div id="comments-container-50250" class="comments-container">
<span id="50302"></span>
<div id="comment-50302" class="comment">
<div id="post-50302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not yet a self answer but making some progress. I have downloaded JOSM and I am now exploring this editor. I can output a pdf formatted image of a plan from QCAD. I can import the image in JOSM. I can view the image in the right side bar. I can't get the image to display in the window used for editing the OSM data.</p>
<p>I think it may have something to do with giving co-ordinates to the pdf image so that it appears in the area I am editing.</p>
<p>Can anybody throw any light on how to display an image within the editor and 'scale' it to be at the same 'zoom' as the OSM map?</p>
</div>
<div id="comment-50302-info" class="comment-info">
<span class="comment-age">(18 Jun '16, 15:48)</span> <span class="comment-user userinfo">bwallum</span>
</div>
</div>
</div>
<div id="comment-tools-50250" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50250-form-container" class="comment-form-container">
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

<span id="50304"></span>

<div id="answer-container-50304" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50304-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50304-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50304-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have found a solution.</p>
<p>Go to Imagery&gt;Imagery Preferences in JOSM editor. Click on the 'Configure available plug-ins' button in the left side bar (icon is a plug and socket). Find the DxFimport plugin, select, update list of plugins (the plugin will be downloaded) and restart JOSM.</p>
<p>When JOSM comes back up make a new layer with File&gt;New Layer. With your new layer active, open your dxf file with File&gt;Open... and browse for the file.</p>
<p>You will be asked for a scale. Default is 1 unit equals 1m on OSM. If you work in millimetres in your dxf work then you set the scale to 1000 units equals 1m at the prompt. Click OK and hey presto, the image is rendered as an imagery layer and can be manipulated.</p>
<p>Works very nicely. No circles in OSM so these are rendered as multi point ways. Accuracy is great.</p>
<p>I have solved this for myself using the excellent plugin by Adrian (asrianCron) and hope this solution may be of value to others.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Jun '16, 21:26</strong></p>
<img src="https://secure.gravatar.com/avatar/2ef546bdea56f93f4203f7b581a6c6b7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="bwallum&#39;s gravatar image" />
<p><span>bwallum</span><br />
<span class="score" title="66 reputation points">66</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="bwallum has one accepted answer">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '16, 21:40</strong> </span></p>
</div>
</div>
<div id="comments-container-50304" class="comments-container">
&#10;</div>
<div id="comment-tools-50304" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50304-form-container" class="comment-form-container">
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

