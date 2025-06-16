+++
type = "question"
title = "[closed] Alignment styling bug in website for /browse/objecttype/id"
description = '''The pages dsplayed at &quot;https://www.openstreetmap.org/browse/object-type/id&quot; has a small problem isible on the French version : some h4 elements are aligned in the second column, because the h4 section above it takes two lines but the infos displayed on the next column only takes one line. Note that h...'''
date = "2013-08-10T15:26:00Z"
lastmod = "2013-08-12T13:59:00Z"
weight = 25163
keywords = [ "website", "css" ]
aliases = [ "/questions/25163" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Alignment styling bug in website for /browse/objecttype/id](/questions/25163/alignment-styling-bug-in-website-for-browseobjecttypeid)

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
<span id="post-25163-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25163-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-25163-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>The pages dsplayed at "https://www.openstreetmap.org/browse/<strong><em>object-type/id</em></strong>" has a small problem isible on the French version : some h4 elements are aligned in the second column, because the h4 section above it takes two lines but the infos displayed on the next column only takes one line.</p>
<p>Note that h4 does not use a standard "display:block" but a "display:inline-block" which means tht it won't fill the rest of the line, but it may still contain line-wraps when its content does not for in the margins of the colum. The HTML structure is:</p>
<pre><code>&lt;div id=&quot;browse-section&quot;&gt;
    &lt;div&gt;
        &lt;h4&gt;Displayed header1&lt;/h4&gt;
        &lt;p&gt;Displayed value1&lt;/p&gt;
    &lt;/div&gt;
    &lt;!-- ... --&gt;
    &lt;div&gt;
        &lt;h4&gt;Displayed header2&lt;/h4&gt;
        &lt;p&gt;Displayed value2&lt;/p&gt;
    &lt;/div&gt;
&lt;/div&gt;</code></pre>
<p>The bug occurs for the (too long) header "Dans le groupe de modification" (in English, this is "In changeset" which fits on a single line) which requires two lines in French (possibly other languages as well) when the value is just a single value. The next section just below it (displaying the value of the changeset comment with the header being "Commentaire") is then incorrectly formatted.</p>
<p>To fix this presentation bug, you just need to add this simple CSS rule:</p>
<pre><code>.browse-section&gt;div {
    clear: left;
}</code></pre>
<p>This forces the current flowing position to be below the height of the displayed lines of the header (when they wraps).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-website" rel="tag" title="see questions tagged &#39;website&#39;">website</span> <span class="post-tag tag-link-css" rel="tag" title="see questions tagged &#39;css&#39;">css</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Aug '13, 15:26</strong></p>
<img src="https://secure.gravatar.com/avatar/b0ac3d0a15ce4f96f0d6b29172fca72a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Verdy_p&#39;s gravatar image" />
<p><span>Verdy_p</span><br />
<span class="score" title="141 reputation points">141</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Verdy_p has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>10 Aug '13, 17:26</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span></p>
</div>
</div>
<div id="comments-container-25163" class="comments-container">
<span id="25224"></span>
<div id="comment-25224" class="comment">
<div id="post-25224-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The github is not accessible. I give it here so that is seen by someone having access to it. I do not expect a response and trhis site is the "HELP and SUPPORT" site, and NOT specific for asking questions. I ask for HELP to maintainers of the OSM site, even if this does not interest YOU, it interests others.</p>
</div>
<div id="comment-25224-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 10:32)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="25225"></span>
<div id="comment-25225" class="comment">
<div id="post-25225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And stop replying with such JUNK. You're not useful at all and you desserve the project when playng the role of the censor here !</p>
</div>
<div id="comment-25225-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 10:43)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="25226"></span>
<div id="comment-25226" class="comment">
<div id="post-25226-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Bug reports don't belong here. Just go to <a href="https://github.com/openstreetmap/openstreetmap-website">https://github.com/openstreetmap/openstreetmap-website</a> create a separate account and start a new issue.</p>
</div>
<div id="comment-25226-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 11:01)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="25227"></span>
<div id="comment-25227" class="comment">
<div id="post-25227-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>My comment was both a question to site developers or people working with them, and an answer to the problem (I give the solution). It was and it is still accurate in the symtiom description and in the solution. You may think it is not important if you use the Englihs locale, both others will think differently. At least ou should have checked the problem and seen it by yourself instead of closing it stupidly without even looking at it.</p>
</div>
<div id="comment-25227-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 11:11)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="25229"></span>
<div id="comment-25229" class="comment">
<div id="post-25229-score" class="comment-score">
4
</div>
<div class="comment-text">
<p>What you wrote is a very good bug report. Unfortunately, bug reports are not the topic of this help-q&amp;a-site. See the FAQ for this site, where bug reports are specifically mentioned as not belonging on this site ( <a href="https://help.openstreetmap.org/faq/">https://help.openstreetmap.org/faq/</a> ). This is the reason your "question" was closed. If you had been nicer in your wording, probably someone would have been willing to transfer your report to github.</p>
</div>
<div id="comment-25229-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 11:49)</span> <span class="comment-user userinfo">gormo</span>
</div>
</div>
<span id="25236"></span>
<div id="comment-25236" class="comment not_top_scorer">
<div id="post-25236-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was nice in my message, but the response that was given to me was clearly non nice. This Help site is the only one diredtly relected to the OSM site. There's NO place directly linked to discuss its own bugs except THIS one. My message was bith a HELP request to have the issue solved, and was also providing HELP/ANSWER on how to fix it. This came here because I cannot fix it myself, and someone must consider it. Totally on topic, Why do you think that people must only give questions to you (those that interest you as you were were alone to decide what to do)?</p>
</div>
<div id="comment-25236-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 13:54)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
<span id="25237"></span>
<div id="comment-25237" class="comment not_top_scorer">
<div id="post-25237-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why do you want to fragment what is in fact help and support? Closing the issue was not the good reply to do. Adding in addition a negative point was then aggressive. Thnik more globally, please.</p>
</div>
<div id="comment-25237-info" class="comment-info">
<span class="comment-age">(12 Aug '13, 13:59)</span> <span class="comment-user userinfo">Verdy_p</span>
</div>
</div>
</div>
<div id="comment-tools-25163" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-25163-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Please use github or trac for bug reports; this site is for questions and answers" by Richard 10 Aug '13, 17:26

</div>

</div>

</div>

