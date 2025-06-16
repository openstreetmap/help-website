+++
type = "question"
title = "Tag tram tracks with name=*, ref=* - or use Relation:route?"
description = '''As a related question to Does the name tag make sense for a tram track?: Is it a good idea at all to use name=* and especially ref=* on tram tracks? Usually (at least in Germany where I live) tram tracks themselves do not have names or numbers -- only the tram lines which run over them do. People do...'''
date = "2011-01-29T16:16:00Z"
lastmod = "2011-03-10T16:58:00Z"
weight = 2545
keywords = [ "tram", "route", "public-transport", "tagging", "relations" ]
aliases = [ "/questions/2545" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tag tram tracks with name=\*, ref=\* - or use Relation:route?](/questions/2545/tag-tram-tracks-with-name-ref-or-use-relationroute)

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
<span id="post-2545-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2545-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-2545-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>As a related question to <a href="/questions/2307/does-the-name-tag-make-sense-for-a-tram-track">Does the name tag make sense for a tram track?</a>:</p>
<p>Is it a good idea at all to use name=* and especially ref=* on tram tracks?</p>
<p>Usually (at least in Germany where I live) tram tracks themselves do not have names or numbers -- only the tram lines which run over them do. People don't say "that is the tram track 632", they say "tram 632 runs there".</p>
<p>At present the wiki for <a href="https://wiki.openstreetmap.org/wiki/Tag:railway%3Dtram">railway=tram</a> recommends to use name=/ref= for the line name/reference.</p>
<p>It seems to me that name (if applicable) and number of a tram line are better mapped using the relation "route" (see <a href="https://wiki.openstreetmap.org/wiki/Relation:route">Relation:route</a>).</p>
<ul>
<li>It is the established mechanism for mapping public transport lines (I believe)</li>
<li>It makes it easier to find the complete extent of a line - if you use name=* on the track, software must piece together all tracks with the same name to find the line (and what about misspelled names?)</li>
<li>There may be two different lines with the same name (e.g. in neighbouring cities); these can only be kept distinct using relations</li>
<li>Commonly more than one line runs on a single track - there's no way to tag this using name=*/ref=*.</li>
</ul>
<p>So wouldn't it be better to change the wiki so it discourages use of name=*/ref=* for tram tracks, and recommends relations instead?</p>
<p>Of course, if a certain track itself is known by a name, that would be ok to tag as such.</p>
<p>Proposed wording:</p>
<blockquote>
<p>To tag which tram lines run over the tag, use a Relation:route.</p>
<p>name=* and ref=* should only be used if the track itself has a name or a designation, independent of the tram lines running over it (which is relatively uncommon, at least in most parts of Europe).</p>
</blockquote>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tram" rel="tag" title="see questions tagged &#39;tram&#39;">tram</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-relations" rel="tag" title="see questions tagged &#39;relations&#39;">relations</span>
</div>
<div id="question-controls" class="post-controls">
<div class="community-wiki">
This question is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Jan '11, 16:16</strong></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sleske has 19 accepted answers">24%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Jan '11, 16:19</strong> </span></p>
</div>
</div>
<div id="comments-container-2545" class="comments-container">
<span id="3699"></span>
<div id="comment-3699" class="comment">
<div id="post-3699-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Don't forget to accept an answer (the round checkmark button).</p>
</div>
<div id="comment-3699-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 16:58)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-2545" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2545-form-container" class="comment-form-container">
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

<span id="3387"></span>

<div id="answer-container-3387" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3387-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3387-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-3387-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would use the ref= tag to indicate which track in a multi-track set if the track number is known, not for the route that travels on that track. If the properties apply to the physical way, it belongs on the way. If it's a route, it belongs in a relation. The only widely accepted exception to this is ref= tags on highways to indicate route numbers, largely due to early limitations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Feb '11, 20:13</strong></p>
<img src="https://secure.gravatar.com/avatar/666698a7b13e402aba7e1e0f6de7c1d3?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Baloo%20Uriza&#39;s gravatar image" />
<p><span>Baloo Uriza</span><br />
<span class="score" title="3180 reputation points"><span>3.2k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Baloo Uriza has 12 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-3387" class="comments-container">
<span id="3388"></span>
<div id="comment-3388" class="comment">
<div id="post-3388-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why some people argue so vehemently against fixing the highway ref= problem is beyond my comprehension...</p>
</div>
<div id="comment-3388-info" class="comment-info">
<span class="comment-age">(25 Feb '11, 20:13)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-3387" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3387-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="2547"></span>

<div id="answer-container-2547" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-2547-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-2547-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-2547-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This help board is meant for "how do I ..." style questions not for discussions on policy. Please use the mailing lists for that and document the arguments on the corresponding wiki talk page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Jan '11, 16:28</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-2547" class="comments-container">
<span id="2549"></span>
<div id="comment-2549" class="comment">
<div id="post-2549-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>This rather surprises me. The FAQ just says "questions should be relevant to this community. So they should be about OpenStreetMap and using OpenStreetMap data." - no mention about "how to" versus "policy". At any rate, I didn't want to start a discussion, I'm just asking whether there is a consensus.</p>
</div>
<div id="comment-2549-info" class="comment-info">
<span class="comment-age">(29 Jan '11, 16:54)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="2550"></span>
<div id="comment-2550" class="comment">
<div id="post-2550-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>If you feel questions about policy are inappropriate here, maybe you could update the FAQ? Otherwise people will be frustrated because they put effort into asking questions here, only to have them shot down.</p>
</div>
<div id="comment-2550-info" class="comment-info">
<span class="comment-age">(29 Jan '11, 16:55)</span> <span class="comment-user userinfo">sleske</span>
</div>
</div>
<span id="3371"></span>
<div id="comment-3371" class="comment">
<div id="post-3371-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Questions about existing policies are fine. Discussions about new policies or changes to exisiting ones are the problem. They don't have a short and clear answer and will lead to longwinded thread that this help board is not suited for.</p>
</div>
<div id="comment-3371-info" class="comment-info">
<span class="comment-age">(25 Feb '11, 10:52)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
</div>
<div id="comment-tools-2547" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-2547-form-container" class="comment-form-container">
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

