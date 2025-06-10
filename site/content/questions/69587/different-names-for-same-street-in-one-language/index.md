+++
type = "question"
title = "Different names for same street in one language"
description = '''I&#x27;m new to OSM and I&#x27;m editing OSM for Israel at the web editor.  Often there are multiple ways to write the street names in English, and sometimes even in Hebrew (often due to political orientations). For example Salameh street can be written as either סלמה or שלמה.  In English it is written as eit...'''
date = "2019-06-12T02:26:00Z"
lastmod = "2019-06-12T15:15:00Z"
weight = 69587
keywords = [ "streetnames", "language" ]
aliases = [ "/questions/69587" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Different names for same street in one language](/questions/69587/different-names-for-same-street-in-one-language)

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
<span id="post-69587-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69587-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69587-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to OSM and I'm editing OSM for Israel at the web editor.<br />
Often there are multiple ways to write the street names in English, and sometimes even in Hebrew (often due to political orientations). For example Salameh street can be written as either סלמה or שלמה.<br />
In English it is written as either: Shalma, Salameh or even Shlomo.<br />
I think it would be helpful to add all the street name versions, for if someone search one of these terms, he will find it. For example, in Google maps the road is called 'Shalma Road', but if you search by 'Shlomo Road', it does direct you to it.<br />
But in the web editor I seem to be able to add one street name per language.<br />
Is there a way to add more versions of the street name for the same language?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-streetnames" rel="tag" title="see questions tagged &#39;streetnames&#39;">streetnames</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '19, 02:26</strong></p>
<img src="https://secure.gravatar.com/avatar/32bd06db68f252652a7d43688be9fca3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aikum&#39;s gravatar image" />
<p><span>aikum</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aikum has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>12 Jun '19, 02:28</strong> </span></p>
</div>
</div>
<div id="comments-container-69587" class="comments-container">
&#10;</div>
<div id="comment-tools-69587" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69587-form-container" class="comment-form-container">
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

<span id="69595"></span>

<div id="answer-container-69595" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69595-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69595-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69595-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There is the <a href="https://wiki.openstreetmap.org/wiki/Key:alt_name">alt_name</a> which gives you the possibility to add 1 alternative name. You can e.g. also use alt_name for an alternative name in Hebrew and alt_name:en for 1an alternative name in English.</p>
<p>People have been using all kinds of alt_name variations (alt_name:1 or alt_name_1, etc.) for more alternatives. None of those is documented or supported by data consumers such as Nominatim (AFAIK).</p>
<p>Are those English names, official names, or are they just slightly different translations/transliterations? We typically do not map transliterations.</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Jun '19, 15:15</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span> </br></br></p>
</div>
</div>
<div id="comments-container-69595" class="comments-container">
&#10;</div>
<div id="comment-tools-69595" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69595-form-container" class="comment-form-container">
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

