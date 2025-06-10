+++
type = "question"
title = "How does one insert special characters in an answer in this Help Wiki?"
description = '''I&#x27;m sure I&#x27;m not alone in wondering how to properly format an answer to a question in this Help system. It uses what, to me at least, is an arcane system of markup characters that I love to hate. I was answering another mapper&#x27;s question just now and struggled to find a way to use underscore charact...'''
date = "2017-08-08T20:45:00Z"
lastmod = "2017-08-09T08:13:00Z"
weight = 57516
keywords = [ "formatting", "special", "characters" ]
aliases = [ "/questions/57516" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How does one insert special characters in an answer in this Help Wiki?](/questions/57516/how-does-one-insert-special-characters-in-an-answer-in-this-help-wiki)

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
<span id="post-57516-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57516-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-57516-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm sure I'm not alone in wondering how to properly format an answer to a question in this Help system. It uses what, to me at least, is an arcane system of markup characters that I love to hate.</p>
<p>I was answering another mapper's question just now and struggled to find a way to use underscore characters. In this Help system, an underscore toggles emphasis (or Italics if you prefer), making it tricky to include an actual underscore in the text of your answer. My workaround was to use a space with the old-style HTML underscore command enclosing a space. Now I see that the HTML code: ampersand-pound-95-semicolon,  _  , will do the job better.</p>
<p>In that last sentence, I wanted to include the code for HTML underline toggle but could not include it as an example because it gets treated as an operator, not as plain text. How does one "escape" this action?</p>
<p>I assume there must be a guide to the way this Help system uses HTML codes and how one produces special characters that show up in one's answers. Can you point that out to me?</p>
<p>Thanks for the assistance.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-formatting" rel="tag" title="see questions tagged &#39;formatting&#39;">formatting</span> <span class="post-tag tag-link-special" rel="tag" title="see questions tagged &#39;special&#39;">special</span> <span class="post-tag tag-link-characters" rel="tag" title="see questions tagged &#39;characters&#39;">characters</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '17, 20:45</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>08 Aug '17, 20:49</strong> </span></p>
</div>
</div>
<div id="comments-container-57516" class="comments-container">
&#10;</div>
<div id="comment-tools-57516" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57516-form-container" class="comment-form-container">
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

<span id="57518"></span>

<div id="answer-container-57518" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-57518-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-57518-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-57518-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="AlaskaDave has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There's a "?" above the answer edit box with a <a href="https://daringfireball.net/projects/markdown/syntax">link to information about the formatting syntax</a>, which is some version of Markdown.</p>
<p>To insert a character that is used for formatting, place a backslash (\) before the character. So to generate the \ in that previous sentence I had to insert \\ in my answer text. An underscore would just be \_ but in my answer it looks like \\\_, because \ is also a special character.</p>
<p>Lots of systems that have special characters use \ for escaping them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '17, 22:09</strong></p>
<img src="https://secure.gravatar.com/avatar/c860445e868ebb21da141635a4aa7b06?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maxerickson&#39;s gravatar image" />
<p><span>maxerickson</span><br />
<span class="score" title="12700 reputation points"><span>12.7k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="176 badges"><span class="bronze">●</span><span class="badgecount">176</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maxerickson has 93 accepted answers">32%</span></p>
</div>
</div>
<div id="comments-container-57518" class="comments-container">
<span id="57519"></span>
<div id="comment-57519" class="comment">
<div id="post-57519-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, Max, that's just what I was looking for. By the way, I tried using a single backslash character to escape the underscore and when that didn't work I resorted to using the HTML method. As you point out, I needed three backslashes.</p>
<p>Thanks again.</p>
</div>
<div id="comment-57519-info" class="comment-info">
<span class="comment-age">(08 Aug '17, 22:36)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="57520"></span>
<div id="comment-57520" class="comment">
<div id="post-57520-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Three backslashes should only be necessary to create \_ in the output. A single backslash followed by an underscore should place an underscore in the output.</p>
</div>
<div id="comment-57520-info" class="comment-info">
<span class="comment-age">(08 Aug '17, 23:00)</span> <span class="comment-user userinfo">maxerickson</span>
</div>
</div>
<span id="57521"></span>
<div id="comment-57521" class="comment">
<div id="post-57521-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I misspoke. Looking back at my scribbling I see that I was trying to use a forward slash, not a backslash. I went back a few minutes ago and edited my answer to the other question so I was able to put your info to good use right away.</p>
<p>Thanks again.</p>
</div>
<div id="comment-57521-info" class="comment-info">
<span class="comment-age">(08 Aug '17, 23:23)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="57523"></span>
<div id="comment-57523" class="comment">
<div id="post-57523-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Side note: This help system parses your text client-side (in Javascript) for a preview, and after submitting, your text is parsed server-side (in PHP or whatever) for incorporation in the page text. Both parsers are slighly different; it has happened to me that using an underscore triggered italics in the preview but not the final text.</p>
</div>
<div id="comment-57523-info" class="comment-info">
<span class="comment-age">(09 Aug '17, 08:13)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-57518" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-57518-form-container" class="comment-form-container">
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

