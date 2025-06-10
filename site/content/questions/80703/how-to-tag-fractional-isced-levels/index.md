+++
type = "question"
title = "How to tag fractional ISCED levels"
description = '''Generally, US high schools would be considered upper secondary educational institutions, which is ISCED level 3. However, most US high schools offer grades 9-12, whereas ISCED level 3 is grades 10-13 (see table on table on Key:grades). When tagging isced:level in such cases, is the common practice t...'''
date = "2021-06-24T19:25:00Z"
lastmod = "2021-06-25T07:03:00Z"
weight = 80703
keywords = [ "tagging" ]
aliases = [ "/questions/80703" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [How to tag fractional ISCED levels](/questions/80703/how-to-tag-fractional-isced-levels)

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
<span id="post-80703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80703-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Generally, US high schools would be considered upper secondary educational institutions, which is ISCED level 3. However, most US high schools offer grades 9-12, whereas ISCED level 3 is grades 10-13 (see table on table on <a href="https://wiki.openstreetmap.org/wiki/Key:grades">Key:grades</a>).</p>
<p>When tagging <a href="https://wiki.openstreetmap.org/wiki/Key:isced:level">isced:level</a> in such cases, is the common practice to go with the spirit of the law and tag <code>3</code> or the letter of the law and tag <code>2;3</code>?</p>
<p>In the former case, it seems there'd have to be a line drawn <em>somewhere</em>. For example, how to tag a US middle school that offers grades 5-8 or 4-7? etc.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '21, 19:25</strong></p>
<img src="https://secure.gravatar.com/avatar/642d4814222916ad9aa09f137bf29a9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joel%20Amos&#39;s gravatar image" />
<p><span>Joel Amos</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joel Amos has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '21, 19:36</strong> </span></p>
</div>
</div>
<div id="comments-container-80703" class="comments-container">
&#10;</div>
<div id="comment-tools-80703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80703-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="80705"></span>

<div id="answer-container-80705" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80705-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80705-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-80705-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Joel Amos has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Non-education person reading the docs:</p>
<p>For the details, ISCED2011 uses a 3-digit code, with the 2 digit for general (4) vs vocational (5), and 3rd for the differences. Offering Grade 9 alone should already be 244 for sufficient level completion with direct access to ISCED 3 (there is no duration requirement). Grade 7-8 should be 242 for partial level completion (with Grade 9 being next), since it is a 2-year programme, culminating 8 years from Grade 1 (ISCED 1 start). Grade 7 alone should be 241 for insufficient for either partial and full level completion, failing to meet the 2-year duration requirement. For Grade 5 or 4-5, there's no further classification in ISCED 1, with only 100.</p>
<p>So my guess:<br />
Grade 9-12: <code>=244;344</code><br />
Grade 5-8: <code>=100;242</code><br />
Grade 4-7: <code>=100;241</code></p>
<p>The standard: <a href="http://uis.unesco.org/sites/default/files/documents/international-standard-classification-of-education-isced-2011-en.pdf">http://uis.unesco.org/sites/default/files/documents/international-standard-classification-of-education-isced-2011-en.pdf</a><br />
Guide: <a href="http://uis.unesco.org/sites/default/files/documents/isced-2011-operational-manual-guidelines-for-classifying-national-education-programmes-and-related-qualifications-2015-en_1.pdf">http://uis.unesco.org/sites/default/files/documents/isced-2011-operational-manual-guidelines-for-classifying-national-education-programmes-and-related-qualifications-2015-en_1.pdf</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 21:14</strong></p>
<img src="https://secure.gravatar.com/avatar/76ffbb56c811e8a8ccdd4c28f122399f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kovoschiz&#39;s gravatar image" />
<p><span>Kovoschiz</span><br />
<span class="score" title="2434 reputation points"><span>2.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="47 badges"><span class="bronze">●</span><span class="badgecount">47</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kovoschiz has 22 accepted answers">16%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '21, 21:30</strong> </span></p>
</div>
</div>
<div id="comments-container-80705" class="comments-container">
<span id="80707"></span>
<div id="comment-80707" class="comment">
<div id="post-80707-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I appreciate the effort post. I read through the docs and agree with your assessment of the above cases. The part I'm less convinced about is whether it is worthwhile to use the 3-digit codes given 1) they currently have almost no use in the database 2) it would be pretty hard to expect accurate tagging from mappers given all the subtleties in ISCED's definitions. Willing to entertain argumentation, though. Cheers!</p>
</div>
<div id="comment-80707-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 23:50)</span> <span class="comment-user userinfo">Joel Amos</span>
</div>
</div>
<span id="80708"></span>
<div id="comment-80708" class="comment">
<div id="post-80708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>When interpreting Michigan's school data for addition to OSM ( <a href="https://maxerickson.github.io/mischools/">https://maxerickson.github.io/mischools/</a> ), I went with the simple definition:</p>
<p>0: "DevK","DevK-Part","KG","KG-Part","K-Part"</p>
<p>1: "1","2","3","4","5"</p>
<p>2: "6","7","8"</p>
<p>3: "9","10","11","12"</p>
<p>I also ended up directly listing the values in <code>grades</code>, because that doesn't require any interpretation.</p>
</div>
<div id="comment-80708-info" class="comment-info">
<span class="comment-age">(25 Jun '21, 00:22)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="80709"></span>
<div id="comment-80709" class="comment">
<div id="post-80709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/19755/joel-amos"></a><a href="https://help.openstreetmap.org/users/19755/joel-amos">@Joel Amos</a>: Well yes, either you care much about it and start adding 3-digit; or you save the trouble for now and simply use <code>=2;3</code> (even only <code>=3</code> as you have found). The only multi-digit code that seems necessary here is 010 and 020 to distinguish kindergarten and preschool. There is an official classification list for the standard programmes <a href="http://uis.unesco.org/en/isced-mappings">http://uis.unesco.org/en/isced-mappings</a> .</p>
</div>
<div id="comment-80709-info" class="comment-info">
<span class="comment-age">(25 Jun '21, 07:03)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-80705" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80705-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="80704"></span>

<div id="answer-container-80704" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-80704-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-80704-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-80704-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>From querying <a href="https://overpass-turbo.eu/s/18Ou">US schools with the <code>isced:level</code> tag with "High School" in the name and "Junior" not in the name</a>, I got ~600 results with roughly 90% using <code>isced:level=3</code>. So it seems most are going by the spirit of the law.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>24 Jun '21, 20:16</strong></p>
<img src="https://secure.gravatar.com/avatar/642d4814222916ad9aa09f137bf29a9a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Joel%20Amos&#39;s gravatar image" />
<p><span>Joel Amos</span><br />
<span class="score" title="51 reputation points">51</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Joel Amos has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jun '21, 21:02</strong> </span></p>
</div>
</div>
<div id="comments-container-80704" class="comments-container">
<span id="80706"></span>
<div id="comment-80706" class="comment">
<div id="post-80706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Feels more like no one looked into it yet, from being the details or a lack of consensus.</p>
</div>
<div id="comment-80706-info" class="comment-info">
<span class="comment-age">(24 Jun '21, 21:32)</span> <span class="comment-user userinfo">Kovoschiz</span>
</div>
</div>
</div>
<div id="comment-tools-80704" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-80704-form-container" class="comment-form-container">
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

