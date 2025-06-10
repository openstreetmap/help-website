+++
type = "question"
title = "How to mass-change tag value"
description = '''Hi, In the Nantes city for public transport we have two values of the tag networks that are used. On the &#x27;terrain&#x27; the real value displayed every where is &#x27;TAN&#x27; but 50% of the relations are tagged with &#x27;fr_tan&#x27;. https://taginfo.openstreetmap.org/tags/network=fr_tan#map What is the best way to migrat...'''
date = "2014-09-02T11:16:00Z"
lastmod = "2014-09-02T12:23:00Z"
weight = 36501
keywords = [ "mass_tagging", "editing", "tagging" ]
aliases = [ "/questions/36501" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to mass-change tag value](/questions/36501/how-to-mass-change-tag-value)

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
<span id="post-36501-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36501-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36501-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>In the Nantes city for public transport we have two values of the tag networks that are used.</p>
<p>On the 'terrain' the real value displayed every where is 'TAN' but 50% of the relations are tagged with 'fr_tan'. <a href="https://taginfo.openstreetmap.org/tags/network=fr_tan#map">https://taginfo.openstreetmap.org/tags/network=fr_tan#map</a></p>
<p>What is the best way to migrate those values to 'TAN' ?</p>
<p>Do someone has already done a script for this ? is their an existing tool to do that ? jOSM ?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mass_tagging" rel="tag" title="see questions tagged &#39;mass_tagging&#39;">mass_tagging</span> <span class="post-tag tag-link-editing" rel="tag" title="see questions tagged &#39;editing&#39;">editing</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Sep '14, 11:16</strong></p>
<img src="https://secure.gravatar.com/avatar/701719480c3577dbfe180e1a08eea462?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="toutpt&#39;s gravatar image" />
<p><span>toutpt</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="toutpt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '14, 12:25</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-36501" class="comments-container">
&#10;</div>
<div id="comment-tools-36501" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36501-form-container" class="comment-form-container">
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

<span id="36502"></span>

<div id="answer-container-36502" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36502-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36502-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36502-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, using JOSM (possibly together with Overpass API, see also the link to it on the taginfo page) seems to be sufficient here (see <span>that other question for example</span>). However, I think that if you plan to use this feature you first should get to know the editor and know yourself how to use it for such mass-retagging.</p>
<p>However, please do not just do it yourself/alone, for various reasons. See <a href="https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct">https://wiki.openstreetmap.org/wiki/Automated_Edits_code_of_conduct</a> and <a href="https://wiki.openstreetmap.org/wiki/Mechanical_Edit_Policy">https://wiki.openstreetmap.org/wiki/Mechanical_Edit_Policy</a> .</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Sep '14, 12:23</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 Sep '14, 12:29</strong> </span></p>
</div>
</div>
<div id="comments-container-36502" class="comments-container">
&#10;</div>
<div id="comment-tools-36502" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36502-form-container" class="comment-form-container">
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

