+++
type = "question"
title = "T r a n s l a t e"
description = '''Is there any translation project? I would like to participate in the translation of Portuguese Brazil'''
date = "2014-03-09T23:18:00Z"
lastmod = "2014-03-09T23:53:00Z"
weight = 30632
keywords = [ "translate" ]
aliases = [ "/questions/30632" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [T r a n s l a t e](/questions/30632/t-r-a-n-s-l-a-t-e)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30632-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Is there any translation project? I would like to participate in the translation of Portuguese Brazil</p></div><div id="question-tags" class="tags-container tags">translate</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>09 Mar '14, 23:18</strong></p><img src="https://secure.gravatar.com/avatar/f4bf7782f003a48161a661d3cca73aa9?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alisson%20Eduardo%20Dos%20Santos&#39;s gravatar image" /><p>Alisson Edua...<br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alisson Eduardo Dos Santos has no accepted answers">0%</span></p></div></div><div id="comments-container-30632" class="comments-container"></div><div id="comment-tools-30632" class="comment-tools"></div><div class="clear"></div><div id="comment-30632-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="30633"></span>

<div id="answer-container-30633" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-30633-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>There's kind of one. To translate all the dissector output would be unreasonable (see the wiki page about it <a href="http://wiki.wireshark.org/Development/Translations">here</a>)... but for the user interface stuff (menu, dialogs, etc.) there is support for it in Qt, which is the next GUI for wireshark. Right now it seems there're French, German, and Chinese language files.</p><p>There are detailed instructions <a href="http://anonsvn.wireshark.org/viewvc/trunk/doc/README.qt?revision=53331&amp;view=markup">here</a> if you're adventurous enough to try compiling the source code, and submitting the changes via git for Portuguese.</p><p>Otherwise just browse on the <a href="https://code.wireshark.org/review/gitweb?p=wireshark.git;a=tree;f=ui/qt">git site ui/qt directory</a>, and grab a copy of one of the language files - for example the French language one: <code>qtshark_fr.ts</code>. Make a version of that in Portuguese, saving it as a new file (qtshark_pt.ts?), and attach it to a new bug on <a href="https://bugs.wireshark.org/bugzilla/">bugs.wireshark.org</a>.</p><p>Edit: to make it easier for you, you can also use a GUI program provided for free from Qt called "Qt Linguist", which provides a very nice graphical front-end to the <code>.ts</code> XML file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>09 Mar '14, 23:53</strong></p><img src="https://secure.gravatar.com/avatar/d02f20c18a7742ec73a666f1974bf6dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hadriel&#39;s gravatar image" /><p>Hadriel<br />
<span class="score" title="2652 reputation points"><span>2.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="39 badges"><span class="bronze">●</span><span class="badgecount">39</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hadriel has 30 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 10 Mar '14, 21:47</p></div></div><div id="comments-container-30633" class="comments-container"><span id="30634"></span><div id="comment-30634" class="comment"><div id="post-30634-score" class="comment-score"></div><div class="comment-text"><p>Oh, and "boa sorte!"</p></div><div id="comment-30634-info" class="comment-info"><span class="comment-age">(10 Mar '14, 00:04)</span> Hadriel</div></div><span id="30672"></span><div id="comment-30672" class="comment"><div id="post-30672-score" class="comment-score"></div><div class="comment-text"><p>Or qtshark_pt_BR.ts, just in case, for example, the Iberians speaking Portuguese want a different translation. :-) (I presume Qt has <em>some</em> facility for handling translations that include both language and territory; hopefully, they realise that there needs to be some way to organize translations to support that. :-) :-) :-) :-) :-) :-))</p></div><div id="comment-30672-info" class="comment-info"><span class="comment-age">(10 Mar '14, 21:30)</span> Guy Harris ♦♦</div></div><span id="30673"></span><div id="comment-30673" class="comment"><div id="post-30673-score" class="comment-score"></div><div class="comment-text"><p>Indeed, it apparently supports Portuguese from: Angola, Brazil, Cape Verde, East Timor, Guinea-Bissau, Macau, Mozambique, Portugal, and São Tomé and Príncipe. :)</p></div><div id="comment-30673-info" class="comment-info"><span class="comment-age">(10 Mar '14, 21:45)</span> Hadriel</div></div><span id="30674"></span><div id="comment-30674" class="comment"><div id="post-30674-score" class="comment-score"></div><div class="comment-text"><p>Yes, <a href="http://qt-project.org/doc/qt-4.8/qtranslator.html#load">QTranslator</a> would, for example, fall back on a _fr file if asked for a locale of "fr_FR" and there's no _fr_FR file, so we can use qtshark_fr.ts for France and still have qtshark_fr_CA.ts for Canadian French (and qtshark_fr_CH.ts if the French-speaking Swiss should have a separate translation, etc.).</p></div><div id="comment-30674-info" class="comment-info"><span class="comment-age">(10 Mar '14, 22:06)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-30633" class="comment-tools"></div><div class="clear"></div><div id="comment-30633-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

