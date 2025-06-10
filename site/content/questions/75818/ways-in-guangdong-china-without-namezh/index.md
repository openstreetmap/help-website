+++
type = "question"
title = "Ways in Guangdong, China without name:zh"
description = '''I want to get a list of Chinese names of ways in Guangdong.  Using Overpass API, I have found ways that have name and do not have name:zh. Is this standard for OSM data? I have also found ways that have name in Traditional Chinese (rather than Simplified Chinese, as observed for name:zh elsewhere), ...'''
date = "2020-07-21T00:37:00Z"
lastmod = "2020-07-21T06:10:00Z"
weight = 75818
keywords = [ "name", "names" ]
aliases = [ "/questions/75818" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Ways in Guangdong, China without name:zh](/questions/75818/ways-in-guangdong-china-without-namezh)

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
<span id="post-75818-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75818-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-75818-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to get a list of Chinese names of ways in Guangdong.</p>
<ol>
<li>Using Overpass API, I have found ways that have <code>name</code> and do not have <code>name:zh</code>. Is this standard for OSM data?</li>
<li>I have also found ways that have <code>name</code> in Traditional Chinese (rather than Simplified Chinese, as observed for <code>name:zh</code> elsewhere), a <code>name:yue</code> in ad-hoc/non-standard Cantonese romanization (improper according to <a href="https://wiki.openstreetmap.org/wiki/Multilingual_names">the OSM wiki</a>), and do not have <code>name:zh</code>. Is this standard for OSM data?`</li>
</ol>
<p>If so,</p>
<ol>
<li>What is the recommended way for getting Chinese names?</li>
</ol>
<p>If not,</p>
<ol>
<li>What is to be done to add <code>name:zh</code>?</li>
<li>What is to be done with the improper <code>name:yue</code>? What can I do, or which community members can I contact?</li>
</ol>
<hr />
<p>Overpass API query for 2.:</p>
<pre><code>[out:csv(::id, &quot;name&quot;, &quot;name:yue&quot;, &quot;name:en&quot;; true; &quot;       &quot;)][timeout:25];
relation(911844);map_to_area-&gt;.mySearchArea;
(
  way
  [&quot;name:yue&quot;]
  [!&quot;name:zh&quot;]
  (area.mySearchArea)
  ;
)-&gt;.myWays;
.myWays out tags;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-names" rel="tag" title="see questions tagged &#39;names&#39;">names</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Jul '20, 00:37</strong></p>
<img src="https://secure.gravatar.com/avatar/34b9b2305147ff202ec94032d1e3a270?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tpko156&#39;s gravatar image" />
<p><span>tpko156</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tpko156 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Jul '20, 00:38</strong> </span></p>
</div>
</div>
<div id="comments-container-75818" class="comments-container">
&#10;</div>
<div id="comment-tools-75818" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75818-form-container" class="comment-form-container">
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

<span id="75820"></span>

<div id="answer-container-75820" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-75820-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-75820-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-75820-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="tpko156 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In general there is no requirement that if the name tag is in a specific language the corresponding language tag exists with the same name. Particularly when we are talking about objects, in this case roads, that likely only have a name in the local language and there will be no other entries.</p>
<p>Outside of that it is up to the local community what they "always" wanted to add, which in the case of China is naturally a bit difficult. As to name:yue : if the values can be generated mechanically, it makes little sense to add them, which however doesn't man that mass deleting them is necessary or a good idea.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Jul '20, 06:10</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-75820" class="comments-container">
&#10;</div>
<div id="comment-tools-75820" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-75820-form-container" class="comment-form-container">
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

</hr>

</div>

</div>

