+++
type = "question"
title = "I can&#x27;t understand how partial matches work in Nominatim"
description = '''I can&#x27;t understand how partial matches work in Nominatim. For example, let&#x27;s take a look at Sesame Lane Childcare Centre in North Lakes, Australia. The following queries contain a partial name of this amenity and find it: Sesame Lane Childcare Centre Sesame Lane Childcare Centre north lakes Sesame n...'''
date = "2015-05-01T17:33:00Z"
lastmod = "2016-06-19T16:09:00Z"
weight = 42789
keywords = [ "search", "nominatim" ]
aliases = [ "/questions/42789" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [I can't understand how partial matches work in Nominatim](/questions/42789/i-cant-understand-how-partial-matches-work-in-nominatim)

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
<span id="post-42789-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42789-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-42789-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I can't understand how partial matches work in Nominatim. For example, let's take a look at <a href="http://www.openstreetmap.org/way/242174537">Sesame Lane Childcare Centre</a> in North Lakes, Australia. The following queries contain a partial name of this amenity and find it:</p>
<pre><code>Sesame Lane Childcare Centre
Sesame Lane Childcare Centre north lakes
Sesame north lakes</code></pre>
<p>But the following do not:</p>
<pre><code>Sesame lane north lakes
Sesame lane childcare north lakes
Sesame lane centre north lakes</code></pre>
<p>In contrary, let's consider <a href="http://www.openstreetmap.org/way/7305241">Palace of Culture and Science</a> in Warsaw, Poland. Every query containing a partial name of this building I tried finds this building:</p>
<pre><code>palace culture warsaw
science culture warsaw
and culture warsaw
palace of science warsaw</code></pre>
<p>I know that</p>
<pre><code>&gt; Nominatim reads queries from left to right</code></pre>
<p>and that full matches are listed before partial matches, and that some keywords such as <code>pub</code> are automatically converted to <code>amenity=pub</code>. Here, only <code>childcare</code> is a keyword but it doesn't explain why even <code>Sesame lane north lakes</code> is not found unless <code>lane</code> itself is also considered special but I am not sure whether it explains a difference between Sesame Lane Childcare Centre and Palace of Culture and Science. Can anybody explain what's the difference between them?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 May '15, 17:33</strong></p>
<img src="https://secure.gravatar.com/avatar/5edb551a82994509450e19fef57cffe5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Arkadiusz%20Drabczyk&#39;s gravatar image" />
<p><span>Arkadiusz Dr...</span><br />
<span class="score" title="101 reputation points">101</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Arkadiusz Drabczyk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42789" class="comments-container">
<span id="50212"></span>
<div id="comment-50212" class="comment">
<div id="post-50212-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can anyone also explain why query such as 'palace culture wars' does not work?</p>
<p>Is there any way to fix this?</p>
</div>
<div id="comment-50212-info" class="comment-info">
<span class="comment-age">(15 Jun '16, 09:30)</span> <span class="comment-user userinfo">Klapsa2503</span>
</div>
</div>
<span id="50312"></span>
<div id="comment-50312" class="comment">
<div id="post-50312-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I don't know the answer, but might be able to suggest further places to read and places to ask.</p>
<p>I'd start with the <a href="http://wiki.openstreetmap.org/wiki/Nominatim">wiki page</a>. That's not guaranteed to be 100% up to date, but it might be helpful. You may be already be aware of the <a href="http://nominatim.openstreetmap.org/search.php?q=Sesame+Lane+Childcare+Centre&amp;polygon=1&amp;viewbox=">direct front-end</a> for Nominatim - you can look at "details" of places that it can find which may help. Issues raised on github such as <a href="https://github.com/twain47/Nominatim/issues/415">this one</a> may also explain some of the inner workings.</p>
<p>With regard to the second part of the question (incomplete word matching) I don't believe that Nominatim does partial word (or misspelling) matching. One that does is <a href="https://mapzen.com/projects/search/?query=&amp;endpoint=autocomplete&amp;lng=-0.12257&amp;lat=51.49667&amp;zoom=12">Pelias</a> by Mapzen - and there may be others.</p>
<p>You could also try asking in #osm or #osm-dev on IRC - people there may know more.</p>
</div>
<div id="comment-50312-info" class="comment-info">
<span class="comment-age">(19 Jun '16, 16:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-42789" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42789-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

