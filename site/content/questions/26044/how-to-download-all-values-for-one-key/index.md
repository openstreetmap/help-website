+++
type = "question"
title = "How to download all values for one key?"
description = '''Hi I am working on a parser for the opening_hours tag. I would like to download all 209.722 values taginfo to search over them with regular expressions and to run the parser on all values. I already tried http://www.overpass-api.de/api/xapi_meta?[opening_hours=] but it returns &quot;runtime error: Query ...'''
date = "2013-09-01T18:19:00Z"
lastmod = "2013-09-08T11:07:00Z"
weight = 26044
keywords = [ "opening_hours" ]
aliases = [ "/questions/26044" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to download all values for one key?](/questions/26044/how-to-download-all-values-for-one-key)

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
<span id="post-26044-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26044-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-26044-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I am working on a <a href="https://github.com/ypid/opening_hours.js/tree/master">parser for the opening_hours tag</a>. I would like to download all 209.722 values <a href="http://taginfo.openstreetmap.org/search?q=opening_hours">taginfo</a> to search over them with regular expressions and to run the parser on all values.</p>
<p>I already tried <a href="http://www.overpass-api.de/api/xapi_meta?">http://www.overpass-api.de/api/xapi_meta?</a><em>[opening_hours=</em>] but it returns "runtime error: Query timed out in "query" at line 3 after 181 seconds.". Does anyone know a second possibility without downloading the planet ;)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-opening_hours" rel="tag" title="see questions tagged &#39;opening_hours&#39;">opening_hours</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Sep '13, 18:19</strong></p>
<img src="https://secure.gravatar.com/avatar/b0829ba878989db13885728a5ae8f2bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ypid&#39;s gravatar image" />
<p><span>ypid</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ypid has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-26044" class="comments-container">
&#10;</div>
<div id="comment-tools-26044" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26044-form-container" class="comment-form-container">
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

<span id="26045"></span>

<div id="answer-container-26045" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26045-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26045-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-26045-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>All right. I found a way using the <a href="http://taginfo.openstreetmap.org/taginfo/apidoc#api_4_key_values">API from taginfo</a>: <a href="http://taginfo.openstreetmap.org/api/4/key/values?key=opening_hours">http://taginfo.openstreetmap.org/api/4/key/values?key=opening_hours</a></p>
<p>You might not want to open this in a browser ;) The returned json is currently 8 Megabyte in size.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '13, 18:25</strong></p>
<img src="https://secure.gravatar.com/avatar/b0829ba878989db13885728a5ae8f2bd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ypid&#39;s gravatar image" />
<p><span>ypid</span><br />
<span class="score" title="106 reputation points">106</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ypid has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Sep '13, 10:59</strong> </span></p>
</div>
</div>
<div id="comments-container-26045" class="comments-container">
<span id="26081"></span>
<div id="comment-26081" class="comment">
<div id="post-26081-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>taginfo also lets you download its .sqlite files which you can then open and search offline.</p>
</div>
<div id="comment-26081-info" class="comment-info">
<span class="comment-age">(02 Sep '13, 20:50)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="26194"></span>
<div id="comment-26194" class="comment">
<div id="post-26194-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks but I am already quite lucky with the way it works. I now have written a simple <a href="https://github.com/ypid/opening_hours.js/blob/feature/regex_search">regex parser</a> which is also integrated with the opening_hours parser (should be easy to adopted for other keys, projects or just to search over some keys). The nice thing with the one API query per key is that I could also integrate it nicely with the <a href="https://github.com/ypid/opening_hours.js/blob/feature/Makefile">Makefile</a> :)</p>
</div>
<div id="comment-26194-info" class="comment-info">
<span class="comment-age">(08 Sep '13, 11:07)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
</div>
<div id="comment-tools-26045" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26045-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="26046"></span>

<div id="answer-container-26046" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26046-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26046-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26046-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can increase the timeout of the Overpass API, see the <a href="http://wiki.openstreetmap.org/wiki/Overpass_API#Osm-Script">Osm-Script</a> section and the <em>timeout</em> attribute.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>01 Sep '13, 18:26</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-26046" class="comments-container">
<span id="26048"></span>
<div id="comment-26048" class="comment">
<div id="post-26048-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks. But after thinking about it, taginfo seems to be the much better source because taginfo already works with this kind of information and has it in an optimized format I guess (at least the download was much faster).</p>
</div>
<div id="comment-26048-info" class="comment-info">
<span class="comment-age">(01 Sep '13, 18:56)</span> <span class="comment-user userinfo">ypid</span>
</div>
</div>
</div>
<div id="comment-tools-26046" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26046-form-container" class="comment-form-container">
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

