+++
type = "question"
title = "Alternative query string don&#x27;t properly work"
description = '''Try this query http://nominatim.openstreetmap.org/search?format=json&amp;amp;postalcode=45400&amp;amp;city=Fleury+les+aubrais&amp;amp;country=fr No result ! Now, without postalcode : http://nominatim.openstreetmap.org/search?format=json&amp;amp;city=Fleury+les+aubrais&amp;amp;country=fr 1 Good result (with postal code ...'''
date = "2013-01-09T20:55:00Z"
lastmod = "2013-01-20T10:38:00Z"
weight = 18940
keywords = [ "postal", "bug" ]
aliases = [ "/questions/18940" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Alternative query string don't properly work](/questions/18940/alternative-query-string-dont-properly-work)

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
<span id="post-18940-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18940-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-18940-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Try this query <a href="http://nominatim.openstreetmap.org/search?format=json&amp;postalcode=45400&amp;city=Fleury+les+aubrais&amp;country=fr">http://nominatim.openstreetmap.org/search?format=json&amp;postalcode=45400&amp;city=Fleury+les+aubrais&amp;country=fr</a> No result !</p>
<p>Now, without postalcode : <a href="http://nominatim.openstreetmap.org/search?format=json&amp;city=Fleury+les+aubrais&amp;country=fr">http://nominatim.openstreetmap.org/search?format=json&amp;city=Fleury+les+aubrais&amp;country=fr</a> 1 Good result (with postal code returned witch is 45400 !!)</p>
<p>In fact, the query parameter "postalcode" don't work ;(</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-postal" rel="tag" title="see questions tagged &#39;postal&#39;">postal</span> <span class="post-tag tag-link-bug" rel="tag" title="see questions tagged &#39;bug&#39;">bug</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jan '13, 20:55</strong></p>
<img src="https://secure.gravatar.com/avatar/dcc2508a57032ce073f8e959037695ff?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fred727&#39;s gravatar image" />
<p><span>fred727</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fred727 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jan '13, 21:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-18940" class="comments-container">
&#10;</div>
<div id="comment-tools-18940" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18940-form-container" class="comment-form-container">
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

<span id="18941"></span>

<div id="answer-container-18941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18941-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This seems to be a bug in Nominatim</p>
<p>Original answer:</p>
<p><em>Try "postcode" not "postalcode". That returns something for me that looks plausibly JSON!</em></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jan '13, 21:04</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Jan '13, 14:00</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/1fe9a0c696a5000fb304ababea9f83af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Sanderd17&#39;s gravatar image" />
<p><span>Sanderd17</span><br />
<span class="score" title="1111 reputation points"><span>1.1k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span></p>
</div>
</div>
<div id="comments-container-18941" class="comments-container">
<span id="18942"></span>
<div id="comment-18942" class="comment">
<div id="post-18942-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The <a href="https://wiki.openstreetmap.org/wiki/Nominatim#Parameters">wiki</a> also mentioned <em>postalcode</em> instead of <em>postcode</em>. I <a href="https://wiki.openstreetmap.org/w/index.php?title=Nominatim&amp;action=historysubmit&amp;diff=853806&amp;oldid=832435">fixed</a> it.</p>
</div>
<div id="comment-18942-info" class="comment-info">
<span class="comment-age">(09 Jan '13, 21:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19137"></span>
<div id="comment-19137" class="comment">
<div id="post-19137-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>"postcode" is not a recognized parameter. The documentation speaks about "postalcode" only.</p>
<p>Replace "postcode" by anything else ('foo', 'bar', etc..) and you will see that the result will be the same !</p>
<p>I realy think there is a bug whith "postalcode" parameter. Is there a place tu submit bugs ?</p>
</div>
<div id="comment-19137-info" class="comment-info">
<span class="comment-age">(16 Jan '13, 08:52)</span> <span class="comment-user userinfo">fred727</span>
</div>
</div>
<span id="19140"></span>
<div id="comment-19140" class="comment not_top_scorer">
<div id="post-19140-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There is - it's <a href="https://trac.openstreetmap.org/query?status=new&amp;status=assigned&amp;status=reopened&amp;component=nominatim&amp;order=priority">"trac" for the "nominatim" component</a>. And yes, the <a href="https://trac.openstreetmap.org/ticket/2497">second bug on that list</a> at the time of writing is "Handle or ignore postal code", so it's already been logged.</p>
</div>
<div id="comment-19140-info" class="comment-info">
<span class="comment-age">(16 Jan '13, 10:35)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="19148"></span>
<div id="comment-19148" class="comment">
<div id="post-19148-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@scai</span> : you do a mistake. The good parameter is postalcode not postcode. Try this query : <a href="http://nominatim.openstreetmap.org/search?format=json&amp;postcode=31330&amp;city=Merville&amp;country=fr">http://nominatim.openstreetmap.org/search?format=json&amp;postcode=31330&amp;city=Merville&amp;country=fr</a> "postcode" is specified with value 31330 but an other result with postal code "59660" is returned</p>
<p>The "good" query (with "postalcode" parameter) don't work <a href="http://nominatim.openstreetmap.org/search?format=json&amp;postalcode=31330&amp;city=Merville&amp;country=fr">http://nominatim.openstreetmap.org/search?format=json&amp;postalcode=31330&amp;city=Merville&amp;country=fr</a></p>
<p>Thank you SomeoneElse for the link to the bug list ;)</p>
</div>
<div id="comment-19148-info" class="comment-info">
<span class="comment-age">(16 Jan '13, 20:09)</span> <span class="comment-user userinfo">fred727</span>
</div>
</div>
<span id="19152"></span>
<div id="comment-19152" class="comment">
<div id="post-19152-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>fred727: <a href="https://github.com/twain47/Nominatim/blob/d1a224bad4b5a3b8fdf077b1b67d529abe9d9278/website/search.php#L156">it seems</a> like you are right.</p>
</div>
<div id="comment-19152-info" class="comment-info">
<span class="comment-age">(17 Jan '13, 07:34)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="19215"></span>
<div id="comment-19215" class="comment not_top_scorer">
<div id="post-19215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@scai</span> : The wiki is buggy now... Why don't you fix it to poastALcode ?</p>
</div>
<div id="comment-19215-info" class="comment-info">
<span class="comment-age">(19 Jan '13, 18:22)</span> <span class="comment-user userinfo">fred727</span>
</div>
</div>
<span id="19221"></span>
<div id="comment-19221" class="comment">
<div id="post-19221-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><span>@fred727</span> I already did several days ago.</p>
</div>
<div id="comment-19221-info" class="comment-info">
<span class="comment-age">(20 Jan '13, 10:38)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18941" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-18941-form-container" class="comment-form-container">
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

