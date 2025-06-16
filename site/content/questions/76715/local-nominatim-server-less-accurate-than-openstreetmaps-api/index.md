+++
type = "question"
title = "Local Nominatim Server Less Accurate Than OpenStreetMaps API?"
description = '''My local server doesn&#x27;t return results for an address as simple as &quot;Dalgety Bay, GB&quot;, whereas the OpenStreetMaps API is able to pick that up. It can read &quot;Dalgety Bay, UK&quot;, however. I&#x27;ve imported the entire planet data, tuned the database, employed all the strategies from the Installation Guide. Any...'''
date = "2020-09-19T22:57:00Z"
lastmod = "2020-09-22T20:09:00Z"
weight = 76715
keywords = [ "openstreetmap", "nominatim", "geocoding", "server" ]
aliases = [ "/questions/76715" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Local Nominatim Server Less Accurate Than OpenStreetMaps API?](/questions/76715/local-nominatim-server-less-accurate-than-openstreetmaps-api)

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
<span id="post-76715-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76715-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-76715-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>My local server doesn't return results for an address as simple as "Dalgety Bay, GB", whereas the OpenStreetMaps API is able to pick that up. It can read "Dalgety Bay, UK", however. I've imported the entire planet data, tuned the database, employed all the strategies from the Installation Guide. Any guidance here would be appreciated.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-openstreetmap" rel="tag" title="see questions tagged &#39;openstreetmap&#39;">openstreetmap</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-geocoding" rel="tag" title="see questions tagged &#39;geocoding&#39;">geocoding</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Sep '20, 22:57</strong></p>
<img src="https://secure.gravatar.com/avatar/f8dd6d1f5bf765fbbb3001eb3bdf3f60?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rirhun&#39;s gravatar image" />
<p><span>rirhun</span><br />
<span class="score" title="26 reputation points">26</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rirhun has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-76715" class="comments-container">
<span id="76743"></span>
<div id="comment-76743" class="comment">
<div id="post-76743-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Next day you posted <a href="/questions/76736/nominatim-server-on-gcp-vm-stalls-when-doing-batch-geocoding-through-multiprocessing">https://help.openstreetmap.org/questions/76736/nominatim-server-on-gcp-vm-stalls-when-doing-batch-geocoding-through-multiprocessing</a> so I assume this is solved?</p>
</div>
<div id="comment-76743-info" class="comment-info">
<span class="comment-age">(21 Sep '20, 11:56)</span> <span class="comment-user userinfo">mtmail</span>
</div>
</div>
<span id="76747"></span>
<div id="comment-76747" class="comment">
<div id="post-76747-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not resolved. But ignored for now.</p>
</div>
<div id="comment-76747-info" class="comment-info">
<span class="comment-age">(21 Sep '20, 17:52)</span> <span class="comment-user userinfo">rirhun</span>
</div>
</div>
</div>
<div id="comment-tools-76715" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76715-form-container" class="comment-form-container">
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

<span id="76770"></span>

<div id="answer-container-76770" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-76770-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-76770-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-76770-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><code>GB</code> is one of the country codes. They are normally added to the word list together with all the other default country names when running: <code>./utils/setup.php --create-country-names</code></p>
<p>Normally the command is run as part of the import process. However, given that you restarted the indexing process, you probably accidentally skipped it. Just rerun the command. There is no harm in running it multiple times on the database.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '20, 20:09</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-76770" class="comments-container">
&#10;</div>
<div id="comment-tools-76770" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-76770-form-container" class="comment-form-container">
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

