+++
type = "question"
title = "Geo URI must not contain question mark, but OSM adds one, why?"
description = '''I needed to gather some locations information and instructed people to find Geo URI through the Share feature on the main OSM site. The URIs produced by that feature look like this: geo:51.3686,6.1746?z=16  Now I try to work with that information as GeoURI, but turns out there are no question marks ...'''
date = "2016-02-18T09:49:00Z"
lastmod = "2016-02-18T16:21:00Z"
weight = 48200
keywords = [ "geouri", "share" ]
aliases = [ "/questions/48200" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Geo URI must not contain question mark, but OSM adds one, why?](/questions/48200/geo-uri-must-not-contain-question-mark-but-osm-adds-one-why)

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
<span id="post-48200-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48200-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-48200-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I needed to gather some locations information and instructed people to find Geo URI through the <code>Share</code> feature on the main OSM site. The URIs produced by that feature look like this:</p>
<pre><code>geo:51.3686,6.1746?z=16</code></pre>
<p>Now I try to work with that information as GeoURI, but turns out there are no question marks in <a href="http://tools.ietf.org/html/rfc5870#section-3.3">RFC 5870</a>. Is OSM intentionally does it? Is it some other derived scheme? This question mark (instead of <code>;</code>) breaks compatibility with at least one available Python library for working with GeoURI, possibly more if not all of these libraries.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-geouri" rel="tag" title="see questions tagged &#39;geouri&#39;">geouri</span> <span class="post-tag tag-link-share" rel="tag" title="see questions tagged &#39;share&#39;">share</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Feb '16, 09:49</strong></p>
<img src="https://secure.gravatar.com/avatar/1aaaf77e89ed1b496cefd433400ebf27?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="int_ua&#39;s gravatar image" />
<p><span>int_ua</span><br />
<span class="score" title="275 reputation points">275</span><span title="9 badges"><span class="badge1">●</span><span class="badgecount">9</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="21 badges"><span class="bronze">●</span><span class="badgecount">21</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="int_ua has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Feb '16, 13:55</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-48200" class="comments-container">
<span id="48201"></span>
<div id="comment-48201" class="comment">
<div id="post-48201-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Which OSM Geo URI are you talking about exactly?</p>
</div>
<div id="comment-48201-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 10:13)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="48202"></span>
<div id="comment-48202" class="comment">
<div id="post-48202-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The one in the <code>Share</code> instrument (or panel?)</p>
</div>
<div id="comment-48202-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 10:26)</span> <span class="comment-user userinfo">int_ua</span>
</div>
</div>
<span id="48203"></span>
<div id="comment-48203" class="comment">
<div id="post-48203-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a>: Go to osm.org , go to a place you wish to share, click the "share" icon, see "Geo URI". Apparently there's a <code>?z=</code> ("zoom"?) HTTP-like parameter, which is not defined in the RFC.</p>
</div>
<div id="comment-48203-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 13:21)</span> <span class="comment-user userinfo">Piskvor</span>
</div>
</div>
<span id="48204"></span>
<div id="comment-48204" class="comment">
<div id="post-48204-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I already spotted it after int_ua's explanation :)</p>
</div>
<div id="comment-48204-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 13:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-48200" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48200-form-container" class="comment-form-container">
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

<span id="48205"></span>

<div id="answer-container-48205" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-48205-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48205-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-48205-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="int_ua has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the Geo URIs produced by the "Share" feature do not comply with RFC 5870.</p>
<p>They currently look like this:</p>
<pre><code>geo:51.3686,6.1746?z=16</code></pre>
<p>The part with the question mark is called the "query component", and was intended to work similarly to the query component in an HTTP URL. It was specified in the draft version of RFC 5870 (see e.g. <a href="http://tools.ietf.org/html/draft-mayrhofer-geo-uri-00#section-5.1">http://tools.ietf.org/html/draft-mayrhofer-geo-uri-00#section-5.1</a> ), but was <a href="http://geouri.org/2007/07/06/internet-draft-updated-to-version-01/">dropped before the draft became a standard</a>.</p>
<p>In other worlds, welcome to the world of standards!</p>
<blockquote>
<p>The nice thing about standards is that you have so many to choose from.</p>
</blockquote>
<p><em>Andrew S. Tanenbaum</em></p>
<hr />
<p>Practically speaking, your safest option is probably to just snip off everything after the "?", including the question mark. Standard-compliant geo URIs will not contain a question mark, so stripping it off should be safe.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Feb '16, 13:53</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
</div>
<div id="comments-container-48205" class="comments-container">
<span id="48206"></span>
<div id="comment-48206" class="comment">
<div id="post-48206-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Perfect, thanks. I ended up writing this: <code>tuple(map(float, urlparse(uri).path.split(',')))</code></p>
</div>
<div id="comment-48206-info" class="comment-info">
<span class="comment-age">(18 Feb '16, 16:21)</span> <span class="comment-user userinfo">int_ua</span>
</div>
</div>
</div>
<div id="comment-tools-48205" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-48205-form-container" class="comment-form-container">
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

