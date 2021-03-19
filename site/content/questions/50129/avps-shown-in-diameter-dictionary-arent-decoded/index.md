+++
type = "question"
title = "AVPs shown in Diameter dictionary aren&#x27;t decoded"
description = '''Hello, I have some AVPs missing (unknown) on Wireshark (Windows). I downloaded from there: http://code.metager.de/source/xref/wireshark/diameter/dictionary.xml/?r=9b7aab935cbfde5d93309d5543df5a077d240a21 The dictionary.xml file contains the AVP I need (1074, 1075, 1081, 1082), overwrite the old one,...'''
date = "2016-02-12T03:01:00Z"
lastmod = "2016-02-12T05:51:00Z"
weight = 50129
keywords = [ "diameter", "avp" ]
aliases = [ "/questions/50129" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [AVPs shown in Diameter dictionary aren't decoded](/questions/50129/avps-shown-in-diameter-dictionary-arent-decoded)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50129-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, I have some AVPs missing (unknown) on Wireshark (Windows). I downloaded from there: <a href="http://code.metager.de/source/xref/wireshark/diameter/dictionary.xml/?r=9b7aab935cbfde5d93309d5543df5a077d240a21">http://code.metager.de/source/xref/wireshark/diameter/dictionary.xml/?r=9b7aab935cbfde5d93309d5543df5a077d240a21</a> The dictionary.xml file contains the AVP I need (1074, 1075, 1081, 1082), overwrite the old one, but still wireshark show me these AVPs as unknown. Do I miss something?</p><p>Thanks Lucas</p></div><div id="question-tags" class="tags-container tags">diameter avp</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>12 Feb '16, 03:01</strong></p><img src="https://secure.gravatar.com/avatar/ee6b467de40257b1d1e986aeb2899fc1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Lucas%20Rey&#39;s gravatar image" /><p>Lucas Rey<br />
<span class="score" title="6 reputation points">6</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Lucas Rey has no accepted answers">0%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 12 Feb '16, 06:14</p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span></p></div></div><div id="comments-container-50129" class="comments-container"><span id="50130"></span><div id="comment-50130" class="comment"><div id="post-50130-score" class="comment-score"></div><div class="comment-text"><p>Adding what I seen on wireshark: <a href="http://i.imgur.com/MMHfonA.png">http://i.imgur.com/MMHfonA.png</a></p></div><div id="comment-50130-info" class="comment-info"><span class="comment-age">(12 Feb '16, 03:22)</span> Lucas Rey</div></div></div><div id="comment-tools-50129" class="comment-tools"></div><div class="clear"></div><div id="comment-50129-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="50138"></span>

<div id="answer-container-50138" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-50138-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Hi, I'm not sure what you mean by "The dictionary.xml file contains the AVP I need" if I look at the file you refere to AVP 1082 is for 3GPP where as the screenshot shows an Ericsson AVP so that XML file will not translate an Ericsson AVP. If you know the the format of Ericsson AVP 1082 you should add it in the file Ericsson.xml with vendor id Ericsson.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>12 Feb '16, 05:51</strong></p><img src="https://secure.gravatar.com/avatar/2d3d425a7a829209431fb38d326b53af?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Anders&#39;s gravatar image" /><p>Anders ♦<br />
<span class="score" title="4578 reputation points"><span>4.6k</span></span><span title="9 badges"><span class="silver">●</span><span class="badgecount">9</span></span><span title="52 badges"><span class="bronze">●</span><span class="badgecount">52</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Anders has 56 accepted answers">17%</span></p></div></div><div id="comments-container-50138" class="comments-container"><span id="50141"></span><div id="comment-50141" class="comment"><div id="post-50141-score" class="comment-score"></div><div class="comment-text"><p>I'd also suggest that if you do know the format of the AVPs you should also <a href="https://wiki.wireshark.org/Development/SubmittingPatches">submit them to Wireshark</a> for inclusion. That way you won't have to re-add them to the XML file every time you upgrade Wireshark.</p><p>If git and Gerrit look too daunting you could always just attach your patch (changes) to a <a href="https://bugs.wireshark.org">bug report</a>.</p></div><div id="comment-50141-info" class="comment-info"><span class="comment-age">(12 Feb '16, 06:14)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-50138" class="comment-tools"></div><div class="clear"></div><div id="comment-50138-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

