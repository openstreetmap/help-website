+++
type = "question"
title = "Extracting Address from XML"
description = '''Hello everyone, I&#x27;m looking at the OpenStreetMap XML and I&#x27;m trying to find my home. If I do a search on the main page, it correctly finds it and points to my house w/ an arrow. If I download the data as OpenStreetMap XML, I don&#x27;t see the actual home addresses there. How does this work? Thanks, mj [...'''
date = "2011-05-02T15:05:00Z"
lastmod = "2011-05-03T05:31:00Z"
weight = 4929
keywords = [ "address" ]
aliases = [ "/questions/4929" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Extracting Address from XML](/questions/4929/extracting-address-from-xml)

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
<span id="post-4929-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4929-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4929-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone,</p>
<p>I'm looking at the OpenStreetMap XML and I'm trying to find my home. If I do a search on the main page, it correctly finds it and points to my house w/ an arrow. If I download the data as OpenStreetMap XML, I don't see the actual home addresses there.</p>
<p>How does this work?</p>
<p>Thanks,</p>
<p>mj</p>
<p>[Edit]</p>
<p>I never entered my home via the addr tag. I looked up a more public address of a building in Chicago and I see the addr tag in there. I guess that my little home is just too little to show up in the XML. :)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '11, 15:05</strong></p>
<img src="https://secure.gravatar.com/avatar/91b665b7261ccd0c73a987911c96d95f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jaskiemr&#39;s gravatar image" />
<p><span>jaskiemr</span><br />
<span class="score" title="16 reputation points">16</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jaskiemr has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>02 May '11, 17:22</strong> </span></p>
</div>
</div>
<div id="comments-container-4929" class="comments-container">
<span id="4934"></span>
<div id="comment-4934" class="comment">
<div id="post-4934-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Please edit your original question and tell us whether you have entered the data of your home with the help of the addr-tags ( <a href="http://wiki.openstreetmap.org/wiki/Key:addr">http://wiki.openstreetmap.org/wiki/Key:addr</a> ) or not.</p>
<p>Or give us a permalink to your home building area if you want, then we can investigate further.</p>
</div>
<div id="comment-4934-info" class="comment-info">
<span class="comment-age">(02 May '11, 16:57)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="4940"></span>
<div id="comment-4940" class="comment">
<div id="post-4940-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>One possible reason is that the house numbers are mapped using address interpolation. That is a ways parallel to the road withs tags stating "here are houses 45 47 .... 63" without mapping each single house.</p>
</div>
<div id="comment-4940-info" class="comment-info">
<span class="comment-age">(03 May '11, 05:31)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-4929" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4929-form-container" class="comment-form-container">
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

<span id="4931"></span>

<div id="answer-container-4931" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4931-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4931-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4931-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The answer probably has something do with Nominatim:</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Nominatim">http://wiki.openstreetmap.org/wiki/Nominatim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 May '11, 16:26</strong></p>
<img src="https://secure.gravatar.com/avatar/c2a980da3fdfa1ee2659ad70d1e21f31?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gnurk&#39;s gravatar image" />
<p><span>gnurk</span><br />
<span class="score" title="6114 reputation points"><span>6.1k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="silver">●</span><span class="badgecount">60</span></span><span title="96 badges"><span class="bronze">●</span><span class="badgecount">96</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gnurk has 18 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-4931" class="comments-container">
&#10;</div>
<div id="comment-tools-4931" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4931-form-container" class="comment-form-container">
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

