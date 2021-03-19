+++
type = "question"
title = "install wireshark on solaris 10"
description = '''what are the prerequisites to install wireshark on solaris 10 i am unable to run wireshark on solaris there are some missing packages . Please provide a list of prerequisites for wireshark installation on solaris 10 Regards,'''
date = "2014-05-15T04:52:00Z"
lastmod = "2014-05-15T09:05:00Z"
weight = 32817
keywords = [ "10", "solaris" ]
aliases = [ "/questions/32817" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [install wireshark on solaris 10](/questions/32817/install-wireshark-on-solaris-10)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32817-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>what are the prerequisites to install wireshark on solaris 10</p><p>i am unable to run wireshark on solaris there are some missing packages . Please provide a list of prerequisites for wireshark installation on solaris 10</p><p>Regards,</p></div><div id="question-tags" class="tags-container tags">10 solaris</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>15 May '14, 04:52</strong></p><img src="https://secure.gravatar.com/avatar/8cfb1c42cc0b0302558eed7dd18ea1ce?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ahmad&#39;s gravatar image" /><p>ahmad<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ahmad has no accepted answers">0%</span></p></div></div><div id="comments-container-32817" class="comments-container"></div><div id="comment-tools-32817" class="comment-tools"></div><div class="clear"></div><div id="comment-32817-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="32833"></span>

<div id="answer-container-32833" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-32833-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>Where did you get the Wireshark package? Chances are whoever provided the package also provides the necessary dependencies.</p><p>By far the easiest way to install a Wireshark package is to use one of the services which provide pre-built packages along with their dependencies such as <a href="http://www.opencsw.org/">OpenCSW</a>.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>15 May '14, 09:05</strong></p><img src="https://secure.gravatar.com/avatar/e0564001bb7deb960d5d9d9c1e0ba074?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="JeffMorriss&#39;s gravatar image" /><p>JeffMorriss ♦<br />
<span class="score" title="6219 reputation points"><span>6.2k</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="72 badges"><span class="bronze">●</span><span class="badgecount">72</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="JeffMorriss has 103 accepted answers">27%</span></p></div></div><div id="comments-container-32833" class="comments-container"><span id="32845"></span><div id="comment-32845" class="comment"><div id="post-32845-score" class="comment-score"></div><div class="comment-text"><p>hi jeff, Please can you be precise on what i have to install ? is openCSW a package ? as I see its a website the provides packages . Please I need a precise answer to procees the installaion</p></div><div id="comment-32845-info" class="comment-info"><span class="comment-age">(16 May '14, 00:03)</span> ahmad</div></div><span id="32848"></span><div id="comment-32848" class="comment"><div id="post-32848-score" class="comment-score"></div><div class="comment-text"><p>Where did you get the Wireshark package you have now? Chances are whoever provided it also provides the dependencies required to install it.</p><p>OpenCSW is one place which provides free-software packages for Solaris (including Wireshark). They provide tools which make installation very easy. For example I think the command would be something like <code>pkgadd wireshark</code> (once you have followed their "getting started" directions which includes installing the <code>pkgadd</code> command).</p><p>I can't really provide you a list of required packages because the list varies depending on who is providing the packages. IIRC it takes something like 15-20 packages (most of which are Gtk+ and its dependencies).</p></div><div id="comment-32848-info" class="comment-info"><span class="comment-age">(16 May '14, 08:49)</span> JeffMorriss ♦</div></div><span id="32875"></span><div id="comment-32875" class="comment"><div id="post-32875-score" class="comment-score"></div><div class="comment-text"><p>i got the package from sunfreeware</p></div><div id="comment-32875-info" class="comment-info"><span class="comment-age">(18 May '14, 23:27)</span> ahmad</div></div><span id="32876"></span><div id="comment-32876" class="comment"><div id="post-32876-score" class="comment-score"></div><div class="comment-text"><p>Also OpenCSW doesn't provide me with the wire shark pkg , it directs me to links with no pkg found .</p></div><div id="comment-32876-info" class="comment-info"><span class="comment-age">(18 May '14, 23:34)</span> ahmad</div></div><span id="32900"></span><div id="comment-32900" class="comment"><div id="post-32900-score" class="comment-score">1</div><div class="comment-text"><p>I thought sunfreeware.com was dead. Oh, I guess not quite, it's now unixpackages.com. Hmmm, but it seems you have to pay to download packages from them so I'd suggest giving up on the package you have and go with OpenCSW instead. (The problem is that to install a sunfreeware.com package you'll probably need dependencies from sunfreeware.com and it seems you can't get them--easily anyway--any more.)</p><p>OpenCSW has a <a href="http://www.opencsw.org/packages/CSWwireshark/">page for Wireshark</a> but you can't download from there. Instead you have to follow their <a href="http://www.opencsw.org/manual/for-administrators/getting-started.html">directions</a> to install all of their stuff.</p></div><div id="comment-32900-info" class="comment-info"><span class="comment-age">(19 May '14, 07:44)</span> JeffMorriss ♦</div></div><span id="32950"></span><div id="comment-32950" class="comment not_top_scorer"><div id="post-32950-score" class="comment-score"></div><div class="comment-text"><p>i have the packages , but there is an error when i try to run wireshark :</p><p>'ld.so.1: wireshark: fatal: libgnutls.so.26: version 'GNUTLS_1_4' not found (required by file /usr/local/lib/libwireshark.so.1) ld.so.1: wireshark: fatal: libgnutls.so.26: open failed: No such file or directory'</p><p>can you help ?</p></div><div id="comment-32950-info" class="comment-info"><span class="comment-age">(21 May '14, 05:49)</span> ahmad</div></div><span id="33002"></span><div id="comment-33002" class="comment not_top_scorer"><div id="post-33002-score" class="comment-score"></div><div class="comment-text"><p>That's very odd. All the packages are from openCSW or are you trying to use the sunfreeware Wireshark package? If all the packages are from openCSW then it would appear they've got a build dependency problem--I'd suggest raising the issue to them.</p><p>If you're still trying to use that sunfreeware Wireshark package then, as I said before, it probably won't work so I'd suggest you use 100% OpenCSW.</p><p>Oh, I guess one more idea: if you do <code>ldd wireshark |grep libgnutls</code> does it point to the libgnutls installed by OpenCSW (probably in /usr/local/lib/) or another one? If another one, you might try removing that other one to see if it then picks up the correct libgnutls.</p></div><div id="comment-33002-info" class="comment-info"><span class="comment-age">(22 May '14, 07:50)</span> JeffMorriss ♦</div></div></div><div id="comment-tools-32833" class="comment-tools"><span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a></div><div class="clear"></div><div id="comment-32833-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

