+++
type = "question"
title = "How to tag genitive cases of place names?"
description = '''So, Irish has a genitive case for place names. We&#x27;re starting to translate townlands.ie into Irish (using Transifex), and we&#x27;ll need to use the genitive name in some cases (e.g. &quot;Baronies in Wicklow&quot; would need to use the genitive name of &quot;Wicklow&quot; (FYI &quot;Cill Mhantáin&quot; is gen, &quot;Cill Mhantáin&quot; is nom...'''
date = "2015-10-22T21:36:00Z"
lastmod = "2015-11-13T21:28:00Z"
weight = 46062
keywords = [ "multilingual", "tagging", "name", "language" ]
aliases = [ "/questions/46062" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to tag genitive cases of place names?](/questions/46062/how-to-tag-genitive-cases-of-place-names)

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
<span id="post-46062-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46062-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-46062-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>So, <a href="https://en.wikipedia.org/wiki/Irish_language">Irish</a> has a genitive case for place names. We're starting to translate <a href="http://www.townlands.ie/">townlands.ie</a> into Irish (using <a href="https://www.transifex.com/openstreetmap/irish-townlands/">Transifex</a>), and we'll need to use the genitive name in some cases (e.g. "Baronies in Wicklow" would need to use the genitive name of "Wicklow" (FYI "Cill Mhantáin" is gen, "Cill Mhantáin" is nom.)).</p>
<p><a href="http://www.logainm.ie/">Logainm</a>, the official Irish Placenames Database, has <a href="http://www.logainm.ie/en/inf/proj-xml">released their data under ODbL</a>, and we're going to use that. It lists the genitive name of placenames. So we have a source.</p>
<p>Is there a best way to add the genitive name of a placename? <code>genitive_name:ga</code>?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-multilingual" rel="tag" title="see questions tagged &#39;multilingual&#39;">multilingual</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-name" rel="tag" title="see questions tagged &#39;name&#39;">name</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>22 Oct '15, 21:36</strong></p>
<img src="https://secure.gravatar.com/avatar/16e12e337f6edc3750681492656097ed?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rorym&#39;s gravatar image" />
<p><span>rorym</span><br />
<span class="score" title="5358 reputation points"><span>5.4k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="49 badges"><span class="silver">●</span><span class="badgecount">49</span></span><span title="100 badges"><span class="bronze">●</span><span class="badgecount">100</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rorym has 18 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>23 Oct '15, 09:42</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/6c2dd6a39d3f38f1bb47a8c1fe8325e2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sleske&#39;s gravatar image" />
<p><span>sleske</span><br />
<span class="score" title="4090 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="78 badges"><span class="bronze">●</span><span class="badgecount">78</span></span></p>
</div>
</div>
<div id="comments-container-46062" class="comments-container">
<span id="46063"></span>
<div id="comment-46063" class="comment not_top_scorer">
<div id="post-46063-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe I'm confused - but why would you need two forms of a name (if you're storing "genitive_name:ga" I presume you've also got "name:ga")? I can understand how a place name's spelling might change depending on what part it's playing in a sentence (English is pretty rare in not doing this), but why would you need to store the other cases? For example, I can find "Suomi" ("Finland") in OSM but not e.g. "Suomeen" (something like "something being brought to Finland").</p>
</div>
<div id="comment-46063-info" class="comment-info">
<span class="comment-age">(22 Oct '15, 22:03)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46065"></span>
<div id="comment-46065" class="comment not_top_scorer">
<div id="post-46065-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes we'll also have <code>name:ga</code>. We want to be able to use OSM-the-database to display information about Irish places. Yes it's mostly a spelling/pronouncation change. But I don't think it's automatically computable in all cases. One aspect is automatically computable, and we'll calculate that. But for the non-automatic ways, I can't see any other option than to add it to OSM.</p>
</div>
<div id="comment-46065-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 09:09)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="46069"></span>
<div id="comment-46069" class="comment">
<div id="post-46069-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I wonder how many other languages have irregular placename nouns? A quick web search finds a wikipedia article that suggests Turkish might - <a href="https://en.wikipedia.org/wiki/Turkish_phonology">https://en.wikipedia.org/wiki/Turkish_phonology</a> - but there may be others.</p>
</div>
<div id="comment-46069-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 09:36)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="46072"></span>
<div id="comment-46072" class="comment">
<div id="post-46072-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>German has the same thing and even differing Genitive forms for different purposes (Schwarzwald - des Schwarzwalds Gipfel - Schwarzwälder Kirschtorte) but I seriously doubt OSM would be the right place to store such things. It's not a dictionary.</p>
</div>
<div id="comment-46072-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 09:53)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="46076"></span>
<div id="comment-46076" class="comment not_top_scorer">
<div id="post-46076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How do people know how to pronounce it? I can imagine that not every Irish person knows all townlands in Ireland. So there must be some grammar rules that allow you to convert between the different forms.</p>
<p>In any case, it seems more like a job for a dictionary for me.</p>
<p>You could probably make a dictionary inside your app, derived from the logainm data. Then a string like "Baronies of {{name}}" can be translated to "xxx {{gen_name}}", which will use the correct genetive for all townlands.</p>
</div>
<div id="comment-46076-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 12:01)</span> <span class="comment-user userinfo">Sanderd17</span>
</div>
</div>
<span id="46078"></span>
<div id="comment-46078" class="comment">
<div id="post-46078-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Could you add a foreign key ref to Logainm? In other words, tag logainm_ref=12345, and then people who want to can pull the genitive from that?</p>
</div>
<div id="comment-46078-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 12:22)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="46079"></span>
<div id="comment-46079" class="comment">
<div id="post-46079-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/5/richard">@Richard</a> Yes we're already adding <code>logainm:ref</code> as a 'foreign key', so that is a possibility.</p>
</div>
<div id="comment-46079-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 12:45)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
<span id="46080"></span>
<div id="comment-46080" class="comment">
<div id="post-46080-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> I think Albanian has a separate case marker for "to $PLACE", which is shown on signs (vs the name of the town/city itself).</p>
</div>
<div id="comment-46080-info" class="comment-info">
<span class="comment-age">(23 Oct '15, 13:16)</span> <span class="comment-user userinfo">rorym</span>
</div>
</div>
</div>
<div id="comment-tools-46062" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-46062-form-container" class="comment-form-container">
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

<span id="46572"></span>

<div id="answer-container-46572" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46572-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46572-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46572-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>In Poland we did an import / merging of official PRNG (Państwowy Rejestr Nazw Geograficznych) dataset, and such genitive names if available were tagged with name:genitive. Also, name:adjective was imported (though it's not as comprehensive and apparently was used in PRNG for adjectives that may be tricky.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 21:28</strong></p>
<img src="https://secure.gravatar.com/avatar/b68bcf9f1c4a7921aeee1bb35b0e2784?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="RicoElectrico&#39;s gravatar image" />
<p><span>RicoElectrico</span><br />
<span class="score" title="371 reputation points">371</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="silver">●</span><span class="badgecount">11</span></span><span title="17 badges"><span class="bronze">●</span><span class="badgecount">17</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="RicoElectrico has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Nov '15, 21:32</strong> </span></p>
</div>
</div>
<div id="comments-container-46572" class="comments-container">
&#10;</div>
<div id="comment-tools-46572" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46572-form-container" class="comment-form-container">
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

