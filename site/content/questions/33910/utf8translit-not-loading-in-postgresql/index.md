+++
type = "question"
title = "Utf8translit not loading in postgresql"
description = '''Hi, I already installed the german mapnik style on centos. All went good. Now I&#x27;m trying to install it on Ubuntu 12.04 and 14.04. But every time when I try to load the transliterate function with the command: CREATE FUNCTION transliterate(text) RETURNS text AS &#x27;$libdir/utf8translit&#x27;, &#x27;transliterate&#x27;...'''
date = "2014-06-12T11:49:00Z"
lastmod = "2015-05-06T23:13:00Z"
weight = 33910
keywords = [ "german", "style", "utf8translit", "mapnik" ]
aliases = [ "/questions/33910" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Utf8translit not loading in postgresql](/questions/33910/utf8translit-not-loading-in-postgresql)

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
<span id="post-33910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33910-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-33910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi,</p>
<p>I already installed the german mapnik style on centos. All went good. Now I'm trying to install it on Ubuntu 12.04 and 14.04. But every time when I try to load the transliterate function with the command:</p>
<pre><code>CREATE FUNCTION transliterate(text) RETURNS text AS &#39;$libdir/utf8translit&#39;, &#39;transliterate&#39; LANGUAGE C STRICT;</code></pre>
<p>I get the following message:</p>
<pre><code>FEHLER:  konnte Bibliothek „/usr/lib/postgresql/9.3/lib/utf8translit.so“ nicht laden: /usr/lib/postgresql/9.3/lib/utf8translit.so: undefined symbol: _ZN6icu_4814Transliterator14createInstanceERKNS_13UnicodeStringE15UTransDirectionR10UErrorCode</code></pre>
<p>The icu librarys and dev headers are installed (compiling of utf8translit works). I also tired to install an older libicu release instead of the actual apt distributed one.</p>
<p>Thanks a lot.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-german" rel="tag" title="see questions tagged &#39;german&#39;">german</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-utf8translit" rel="tag" title="see questions tagged &#39;utf8translit&#39;">utf8translit</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>12 Jun '14, 11:49</strong></p>
<img src="https://secure.gravatar.com/avatar/a36cd0da8b4e5004f5a80b4ac57d32a2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="adopin&#39;s gravatar image" />
<p><span>adopin</span><br />
<span class="score" title="11 reputation points">11</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="adopin has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33910" class="comments-container">
<span id="33912"></span>
<div id="comment-33912" class="comment">
<div id="post-33912-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This seems to be a problem of your postgres packages. Are these the official packages shipped with Ubuntu or are they third party packages?</p>
</div>
<div id="comment-33912-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 12:10)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33913"></span>
<div id="comment-33913" class="comment">
<div id="post-33913-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I used the packages of apt.postgresql.org</p>
</div>
<div id="comment-33913-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 12:13)</span> <span class="comment-user userinfo">adopin</span>
</div>
</div>
<span id="33914"></span>
<div id="comment-33914" class="comment">
<div id="post-33914-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In that case you should try to contact the package maintainer(s). The website mentions an IRC channel, a mailing list and multiple email addresses. This isn't an OSM-specific problem. But it would be nice if you could post the solution here afterwards.</p>
</div>
<div id="comment-33914-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 12:18)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33915"></span>
<div id="comment-33915" class="comment">
<div id="post-33915-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I konw that this is not a osm specific problem. But the utf8translit module comes with the german mapnik style so I thought that here could be someone with the same problem.</p>
</div>
<div id="comment-33915-info" class="comment-info">
<span class="comment-age">(12 Jun '14, 12:26)</span> <span class="comment-user userinfo">adopin</span>
</div>
</div>
</div>
<div id="comment-tools-33910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33910-form-container" class="comment-form-container">
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

<span id="42936"></span>

<div id="answer-container-42936" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-42936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-42936-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-42936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A small change in the Makefile solves the problem, see <a href="https://lists.openstreetmap.de/pipermail/mapnik-de/2015-February/000265.html">https://lists.openstreetmap.de/pipermail/mapnik-de/2015-February/000265.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 May '15, 23:13</strong></p>
<img src="https://secure.gravatar.com/avatar/75bf05eeb4e509ab00f592416136d8c9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ugoertz&#39;s gravatar image" />
<p><span>ugoertz</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ugoertz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-42936" class="comments-container">
&#10;</div>
<div id="comment-tools-42936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-42936-form-container" class="comment-form-container">
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

