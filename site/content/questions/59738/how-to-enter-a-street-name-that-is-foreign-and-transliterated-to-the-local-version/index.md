+++
type = "question"
title = "How to enter a street name that is foreign and transliterated to the local version"
description = '''Hello, I&#x27;m mapping a Greek town. My understanding from what I&#x27;ve read here and there is that I should not attempt to translate or transliterate local street names; instead, enter them in Greek only. However, there is a street whose name is of a German&#x27;s, Wilhelm Dörpfeld, and it is locally known tra...'''
date = "2017-09-21T08:22:00Z"
lastmod = "2017-09-25T23:26:00Z"
weight = 59738
keywords = [ "i18n", "internationalization", "translation", "transliteration", "localization" ]
aliases = [ "/questions/59738" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [How to enter a street name that is foreign and transliterated to the local version](/questions/59738/how-to-enter-a-street-name-that-is-foreign-and-transliterated-to-the-local-version)

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
<span id="post-59738-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59738-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-59738-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>I'm mapping a Greek town. My understanding from what I've read here and there is that I should not attempt to translate or transliterate local street names; instead, enter them in Greek only.</p>
<p>However, there is a street whose name is of a German's, Wilhelm Dörpfeld, and it is locally known transliterated to Greek. I guess the main name of the street on OSM must be the Greek-transliterated name, as this is what it's known as locally. But we can't expect automatic tools to transliterate it back to Latin correctly, so I believe the Latin version should also be entered. In what language? German? (In that case English viewers should automatically get the German version instead of the Greek version [whether in the Greek alphabet or transliterated back to Latin], and I'm not certain map renderers are that smart.)</p>
<p>Another option could be to add the main street name in German, and add a Greek transl[iter]ation.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-i18n" rel="tag" title="see questions tagged &#39;i18n&#39;">i18n</span> <span class="post-tag tag-link-internationalization" rel="tag" title="see questions tagged &#39;internationalization&#39;">internationalization</span> <span class="post-tag tag-link-translation" rel="tag" title="see questions tagged &#39;translation&#39;">translation</span> <span class="post-tag tag-link-transliteration" rel="tag" title="see questions tagged &#39;transliteration&#39;">transliteration</span> <span class="post-tag tag-link-localization" rel="tag" title="see questions tagged &#39;localization&#39;">localization</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '17, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/39d2ea0a36d1740e5f544076955a4b30?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aptiko&#39;s gravatar image" />
<p><span>aptiko</span><br />
<span class="score" title="135 reputation points">135</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aptiko has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '17, 08:24</strong> </span></p>
</div>
</div>
<div id="comments-container-59738" class="comments-container">
&#10;</div>
<div id="comment-tools-59738" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59738-form-container" class="comment-form-container">
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

<span id="59754"></span>

<div id="answer-container-59754" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-59754-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-59754-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-59754-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="aptiko has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi,</p>
<p>First of all, set the <code>name=*</code> tag to the street name as it appears on street signs. This is the default name that international renderers will use.</p>
<p>Secondly, add a <code>name:xx</code> tag for the other language. (This matters for searching.) If the name on street signs is in Greek, then add a <code>name:de=Wilhelm Dörpfeld</code> tag to record the German name; if the street signs are in German, use <code>name:el=...</code> with the name transliterated into Greek. You can even add all three of <code>name</code>, <code>name:el</code>, and <code>name:de</code> (two of them would have the same value).</p>
<p>If the street signs name is in Greek, you can additionally record the name in German in the <code>int_name=*</code> tag, to explicitly record the "other preferred" variant of the name. This would help renderers show to non-Greek speakers the German, rather than Greek, spelling of the name. (There is also a <code>loc_name</code> tag for the converse case, but a case could be made that using it would be redundant since renderers should know to look for a <code>name:el</code> tag in Greece.)</p>
<p>See:</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Key:name">https://wiki.openstreetmap.org/wiki/Key:name</a> and <a href="https://wiki.openstreetmap.org/wiki/Names">https://wiki.openstreetmap.org/wiki/Names</a> for various name tags</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Multilingual_names#Greece">https://wiki.openstreetmap.org/wiki/Multilingual_names#Greece</a> for some Greece-specific conventions (not directly applicable here)</p>
<p>HTH!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '17, 20:50</strong></p>
<img src="https://secure.gravatar.com/avatar/8440750fd002fd989ab2e6b613ca3ccb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="dsh4&#39;s gravatar image" />
<p><span>dsh4</span><br />
<span class="score" title="867 reputation points">867</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="13 badges"><span class="silver">●</span><span class="badgecount">13</span></span><span title="30 badges"><span class="bronze">●</span><span class="badgecount">30</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="dsh4 has one accepted answer">4%</span></p>
</div>
</div>
<div id="comments-container-59754" class="comments-container">
<span id="59823"></span>
<div id="comment-59823" class="comment">
<div id="post-59823-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not in this specific case, but generally, <a href="https://wiki.openstreetmap.org/wiki/Multilingual_names#Greece">https://wiki.openstreetmap.org/wiki/Multilingual_names#Greece</a> seems to imply that the transliterated name should be entered in <code>int_name</code>. Is that true? I recall seeing elsewhere that transliterating should be avoided (because it can be done by automated tools).</p>
</div>
<div id="comment-59823-info" class="comment-info">
<span class="comment-age">(25 Sep '17, 12:38)</span> <span class="comment-user userinfo">aptiko</span>
</div>
</div>
<span id="59837"></span>
<div id="comment-59837" class="comment">
<div id="post-59837-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree; that link's suggestion about int_name seems odd for the reason you give and for two other reasons:</p>
<ul>
<li><p>There's a "script code" suffix, e.g., name:latn / name:cyrl for name in Latin / Cyrillic script (used in the Balkan), so conceivably there could be a name:latn / name:[Greek Script code] tag pair instead.</p></li>
<li><p>The documentation of name keys suggests that "int_name" should be about "This feature is internationally known by a name other than its official name", not about transliteration issues.</p></li>
</ul>
<p>I suggest you take this up with the Greek OSM community. See <a href="https://wiki.openstreetmap.org/wiki/WikiProject_Greece#Community">https://wiki.openstreetmap.org/wiki/WikiProject_Greece#Community</a> (and note that the "Names" section on that page repeats the advice about int_name).</p>
</div>
<div id="comment-59837-info" class="comment-info">
<span class="comment-age">(25 Sep '17, 23:26)</span> <span class="comment-user userinfo">dsh4</span>
</div>
</div>
</div>
<div id="comment-tools-59754" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-59754-form-container" class="comment-form-container">
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

