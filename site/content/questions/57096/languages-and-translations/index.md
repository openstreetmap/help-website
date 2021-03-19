+++
type = "question"
title = "Languages and Translations"
description = '''In the folder &#92;Wireshark&#92;translations&#92; there are 16 different language files. The language settings of the program only seven. Why? Where is the translator into Russian, he may need some help?'''
date = "2016-11-07T13:45:00Z"
lastmod = "2016-11-08T01:34:00Z"
weight = 57096
keywords = [ "translate", "language" ]
aliases = [ "/questions/57096" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Languages and Translations](/questions/57096/languages-and-translations)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57096-score" class="post-score" title="current number of votes">0</div><span id="post-57096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>In the folder \Wireshark\translations\ there are 16 different language files. The language settings of the program only seven. Why? Where is the translator into Russian, he may need some help?</p></div><div id="question-tags" class="tags-container tags"><span class="post-tag tag-link-translate" rel="tag" title="see questions tagged &#39;translate&#39;">translate</span> <span class="post-tag tag-link-language" rel="tag" title="see questions tagged &#39;language&#39;">language</span></div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>07 Nov '16, 13:45</strong></p><img src="https://secure.gravatar.com/avatar/4954f9ef2ac01afa6d8cb08f7f0d867f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ssobb&#39;s gravatar image" /><p><span>ssobb</span><br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ssobb has no accepted answers">0%</span></p></div></div><div id="comments-container-57096" class="comments-container"></div><div id="comment-tools-57096" class="comment-tools"></div><div class="clear"></div><div id="comment-57096-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57101"></span>

<div id="answer-container-57101" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><span id="post-57101-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span><div id="post-57101-score" class="post-score" title="current number of votes">0</div><span id="post-57101-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span></div></td><td><div class="item-right"><div class="answer-body"><p>The only actual translated-UI files in the Wireshark source are:</p><pre><code>ui/qt/wireshark_de.ts           ui/qt/wireshark_ja_JP.ts
ui/qt/wireshark_en.ts           ui/qt/wireshark_pl.ts
ui/qt/wireshark_fr.ts           ui/qt/wireshark_zh_CN.ts
ui/qt/wireshark_it.ts</code></pre><p>so that's German, English, French, Italian, Japanese in Japan (as opposed to Japanese somewhere else? Why not just <code>ui/qt/wireshark_ja.ts</code>?), Polish, and Chinese in the People's Republic of China (would zh_TW use Traditional Chinese rather than Simplified Chinese?). There's no <code>ui/qt/wireshark_ru.ts</code>, so there's no Russian translation; I don't think anybody's worked on a translation, so it appears there <em>is</em> no Russian translator. (The Russian I learned in school has been unused for более сорока лет, so I'm not going to volunteer. :-))</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>07 Nov '16, 13:56</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p><span>Guy Harris ♦♦</span><br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></div></div><div id="comments-container-57101" class="comments-container"><span id="57113"></span><div id="comment-57113" class="comment"><div id="post-57113-score" class="comment-score"></div><div class="comment-text"><p>Files <em>.qm it is binary, compiled files</em> .qs? What is it? It looks at the translation files and precompiled binary files *.ts in the source code.</p><p><img src="https://osqa-ask.wireshark.org/upfiles/2016-11-08_064442.png" alt="alt text" /></p></div><div id="comment-57113-info" class="comment-info"><span class="comment-age">(07 Nov '16, 20:54)</span> <span class="comment-user userinfo">ssobb</span></div></div><span id="57114"></span><div id="comment-57114" class="comment"><div id="post-57114-score" class="comment-score"></div><div class="comment-text"><p>Where did that screenshot come from? Perhaps Qt has its <em>own</em> translation files that are included when it's packaged for Windows, but the <em>Wireshark</em> project has only the languages I've mentioned.</p></div><div id="comment-57114-info" class="comment-info"><span class="comment-age">(07 Nov '16, 21:14)</span> <span class="comment-user userinfo">Guy Harris ♦♦</span></div></div><span id="57139"></span><div id="comment-57139" class="comment"><div id="post-57139-score" class="comment-score"></div><div class="comment-text"><p>QT has some predefined translation included (qt_XX files).</p><p>Contribution for translation can be done with Transifex ( <a href="https://www.transifex.com/wireshark/wireshark">https://www.transifex.com/wireshark/wireshark</a> ).</p><p>Currently three persons have joined the Russian translation group. However zero terms have been translated so far.</p><p>Any contribution is welcome!!!</p></div><div id="comment-57139-info" class="comment-info"><span class="comment-age">(08 Nov '16, 01:34)</span> <span class="comment-user userinfo">Uli</span></div></div></div><div id="comment-tools-57101" class="comment-tools"></div><div class="clear"></div><div id="comment-57101-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

