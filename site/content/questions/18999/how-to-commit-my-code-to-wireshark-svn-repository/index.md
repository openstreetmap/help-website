+++
type = "question"
title = "How to commit my code to wireshark SVN repository?"
description = '''My task is add more function to wireshark ,especially the FP RLC RRC and RLCdeciphering. I have basically accomplished the rlc RLC deciphering function. How do to commit my code to the wireshark SVN repository?'''
date = "2013-02-28T18:51:00Z"
lastmod = "2013-02-28T22:07:00Z"
weight = 18999
keywords = [ "svn", "commit", "repository" ]
aliases = [ "/questions/18999" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to commit my code to wireshark SVN repository?](/questions/18999/how-to-commit-my-code-to-wireshark-svn-repository)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-18999-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>My task is add more function to wireshark ,especially the FP RLC RRC and RLCdeciphering.</p><p>I have basically accomplished the rlc RLC deciphering function.</p><p>How do to commit my code to the wireshark SVN repository?</p></div><div id="question-tags" class="tags-container tags">svn commit repository</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>28 Feb '13, 18:51</strong></p><img src="https://secure.gravatar.com/avatar/f6eeed42d5aadabfed2ca2cb1faabff1?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="smilezuzu&#39;s gravatar image" /><p>smilezuzu<br />
<span class="score" title="20 reputation points">20</span><span title="32 badges"><span class="badge1">●</span><span class="badgecount">32</span></span><span title="32 badges"><span class="silver">●</span><span class="badgecount">32</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="smilezuzu has no accepted answers">0%</span></p></div></div><div id="comments-container-18999" class="comments-container"></div><div id="comment-tools-18999" class="comment-tools"></div><div class="clear"></div><div id="comment-18999-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="19007"></span>

<div id="answer-container-19007" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19007-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>I believe <a href="http://www.wireshark.org/docs/wsdg_html_chunked/ChSrcContribute.html">this link</a> explains it.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 20:57</strong></p><img src="https://secure.gravatar.com/avatar/46196bc495ce51058590c4e4ae334d22?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SidR&#39;s gravatar image" /><p>SidR<br />
<span class="score" title="245 reputation points">245</span><span title="12 badges"><span class="badge1">●</span><span class="badgecount">12</span></span><span title="17 badges"><span class="silver">●</span><span class="badgecount">17</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SidR has 3 accepted answers">30%</span></p></div></div><div id="comments-container-19007" class="comments-container"></div><div id="comment-tools-19007" class="comment-tools"></div><div class="clear"></div><div id="comment-19007-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="19012"></span>

<div id="answer-container-19012" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-19012-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Note that Kasumi core deciphering engine cannot be integrated in Wireshark as-is due to patent issues, as I already explained you here: <a href="https://ask.wireshark.org/questions/18161/if-the-new-version-of-wireshark-should-have-the-decipher-function-in-umts_rlc-am-and-um">https://ask.wireshark.org/questions/18161/if-the-new-version-of-wireshark-should-have-the-decipher-function-in-umts_rlc-am-and-um</a></p><p>The development version already have some code in place to ease the integration of this deciphering algorithm. As far as I can remember this was working only in RLC AM mode and not UM, and I'm not sure it was completely polished. Patches in this area are always welcome so you can submit an enhancement bug with your code a sample pcap file.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>28 Feb '13, 22:07</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-19012" class="comments-container"><span id="19196"></span><div id="comment-19196" class="comment"><div id="post-19196-score" class="comment-score"></div><div class="comment-text"><p>On the development version. I have try it ,but the deciphering function is not so good,it completely unable to decipher the ciphering pcap.</p><p>and the FP MAC RLC decode have so many bug that most of frame can't be decode correctly.</p><p>I have fixed some of those bug,but I don't know how to commit it to here,and to which branch?</p></div><div id="comment-19196-info" class="comment-info"><span class="comment-age">(05 Mar '13, 18:52)</span> smilezuzu</div></div><span id="19197"></span><div id="comment-19197" class="comment"><div id="post-19197-score" class="comment-score"></div><div class="comment-text"><p>You have told me the patent about the f8,so I will not commit it to the release version.</p><p>but in the development version,there is have the f8 now.</p></div><div id="comment-19197-info" class="comment-info"><span class="comment-age">(05 Mar '13, 18:55)</span> smilezuzu</div></div><span id="19199"></span><div id="comment-19199" class="comment"><div id="post-19199-score" class="comment-score"></div><div class="comment-text"><p>Open a bug report here <a href="https://bugs.wireshark.org/bugzilla/">https://bugs.wireshark.org/bugzilla/</a> and attach your patches, if possible with a sample trace to verify them with.</p></div><div id="comment-19199-info" class="comment-info"><span class="comment-age">(05 Mar '13, 22:55)</span> Anders ♦</div></div><span id="19200"></span><div id="comment-19200" class="comment"><div id="post-19200-score" class="comment-score"></div><div class="comment-text"><p>Oh, patches against trunk (1.9.1)</p></div><div id="comment-19200-info" class="comment-info"><span class="comment-age">(05 Mar '13, 22:56)</span> Anders ♦</div></div><span id="33928"></span><div id="comment-33928" class="comment"><div id="post-33928-score" class="comment-score"></div><div class="comment-text"><p>Hello, did you able to achieve deciphering ? I couldn't decipher it by placing f8 code in wireshark?</p></div><div id="comment-33928-info" class="comment-info"><span class="comment-age">(18 Jun '14, 06:46)</span> gargoylec</div></div></div><div id="comment-tools-19012" class="comment-tools"></div><div class="clear"></div><div id="comment-19012-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

