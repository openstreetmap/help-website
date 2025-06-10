+++
type = "question"
title = "Partial name matching"
description = '''When I try to search via XML for phrase &quot;sienkiewicza, lodz&quot;: http://nominatim.openstreetmap.org/search/sienkiewicza%2C+lodz?format=xml I get 3 results, none of which is the street Henryka Sienkiewicza in Łódź, which I would expect. Instead, I get 3 other streets named &quot;Henryka Sienkiewicza&quot; in 3 ot...'''
date = "2016-06-08T16:25:00Z"
lastmod = "2016-06-27T14:07:00Z"
weight = 50087
keywords = [ "partial", "name", "matching" ]
aliases = [ "/questions/50087" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Partial name matching](/questions/50087/partial-name-matching)

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
<span id="post-50087-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50087-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-50087-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I try to search via XML for phrase "sienkiewicza, lodz":</p>
<p><a href="http://nominatim.openstreetmap.org/search/sienkiewicza%2C+lodz?format=xml">http://nominatim.openstreetmap.org/search/sienkiewicza%2C+lodz?format=xml</a></p>
<p>I get 3 results, none of which is the street Henryka Sienkiewicza in Łódź, which I would expect. Instead, I get 3 other streets named "Henryka Sienkiewicza" in 3 other cities (Brzeziny, Bełchatów and Konstantynów Łódzki), only because there are bus stops named simply "Sienkiewicza".</p>
<p>Are there any search parameters which would allow matching parts of names?</p>
<p>Nota bene: when I get "More results", the street Henryka Sienkiewicza in Łodź appears, so "More results" is seemingly capable of partial matching. How to enable this functionality in first (i.e. not "More results") search?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-partial" rel="tag" title="see questions tagged &#39;partial&#39;">partial</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-matching" rel="tag" title="see questions tagged &#39;matching&#39;">matching</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Jun '16, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/571be31c6d43aa01864cf7a1b3f1c645?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grzegorzborowiak&#39;s gravatar image" />
<p><span>grzegorzboro...</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grzegorzborowiak has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-50087" class="comments-container">
<span id="50481"></span>
<div id="comment-50481" class="comment">
<div id="post-50481-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answers. I will try to use them, photon seems promising. Is there a more detailed API description (i.e. documentation) for photon?</p>
</div>
<div id="comment-50481-info" class="comment-info">
<span class="comment-age">(27 Jun '16, 14:07)</span> <span class="comment-user userinfo">grzegorzboro...</span>
</div>
</div>
</div>
<div id="comment-tools-50087" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50087-form-container" class="comment-form-container">
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

<span id="50088"></span>

<div id="answer-container-50088" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-50088-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-50088-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-50088-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Try <a href="http://photon.komoot.de/">http://photon.komoot.de/</a></p>
<p>Github: <a href="https://github.com/komoot/photon">https://github.com/komoot/photon</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Jun '16, 16:31</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-50088" class="comments-container">
<span id="50089"></span>
<div id="comment-50089" class="comment">
<div id="post-50089-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>... or see <a href="http://wiki.openstreetmap.org/wiki/Search_engines">http://wiki.openstreetmap.org/wiki/Search_engines</a> in general.</p>
</div>
<div id="comment-50089-info" class="comment-info">
<span class="comment-age">(08 Jun '16, 17:34)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
</div>
<div id="comment-tools-50088" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-50088-form-container" class="comment-form-container">
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

