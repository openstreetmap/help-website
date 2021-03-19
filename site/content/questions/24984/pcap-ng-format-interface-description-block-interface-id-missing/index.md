+++
type = "question"
title = "PCAP-NG format, Interface Description Block: Interface ID missing"
description = '''Reading again the PCAP Next Generation Dump File Format specification, i see a defect in the Interface Description Block paragraph: the figure shows no Interface ID inside the block though this field is described underneath. This was never fixed? Too bad, it would really have been nicer than numerat...'''
date = "2013-09-20T01:11:00Z"
lastmod = "2013-09-20T01:34:00Z"
weight = 24984
keywords = [ "interface", "pcap-ng", "id" ]
aliases = [ "/questions/24984" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [PCAP-NG format, Interface Description Block: Interface ID missing](/questions/24984/pcap-ng-format-interface-description-block-interface-id-missing)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24984-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Reading again the PCAP Next Generation Dump File Format specification, i see a defect in the Interface Description Block paragraph: the figure shows no Interface ID inside the block though this field is described underneath.</p><p>This was never fixed? Too bad, it would really have been nicer than numerating the interfaces by their order in the list of Interfae Description Blocks.</p><p>Or am i missing something?</p></div><div id="question-tags" class="tags-container tags">interface pcap-ng id</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Sep '13, 01:11</strong></p><img src="https://secure.gravatar.com/avatar/0c4a0d3634bb05bf810ee1b5fe13ec54?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ime-braun&#39;s gravatar image" /><p>ime-braun<br />
<span class="score" title="1 reputation points">1</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ime-braun has no accepted answers">0%</span></p></div></div><div id="comments-container-24984" class="comments-container"></div><div id="comment-tools-24984" class="comment-tools"></div><div class="clear"></div><div id="comment-24984-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="24987"></span>

<div id="answer-container-24987" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-24987-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You're right, it is not in the block, but it doesn't have to be. When reading a PCAPng file the first Interface Description Block is interface 0, the second is interface 1, and so on. It is sort of mentioned in the sentence that says</p><p><code>Interface ID: Tools that write / read the capture file associate a progressive 16-bit number (starting from '0') to each Interface Definition Block.</code></p><p>To add an index to the block is not necessary, but of course this means that when reading and writing PCAPng files you must keep the interfaces in the same order, or, if reordering them, renumber the interface IDs in all frames headers accordingly.</p><p>But since I'm going to work on the specifications in the next couple of weeks/months anyway I'll write down a reminder to myself to clarify this in the text.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>20 Sep '13, 01:34</strong></p><img src="https://secure.gravatar.com/avatar/c578ba2967741f25aebd6afef702f432?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jasper&#39;s gravatar image" /><p>Jasper ♦♦<br />
<span class="score" title="23806 reputation points"><span>23.8k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="51 badges"><span class="silver">●</span><span class="badgecount">51</span></span><span title="284 badges"><span class="bronze">●</span><span class="badgecount">284</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jasper has 263 accepted answers">18%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 20 Sep '13, 01:35</p></div></div><div id="comments-container-24987" class="comments-container"><span id="24995"></span><div id="comment-24995" class="comment"><div id="post-24995-score" class="comment-score"></div><div class="comment-text"><blockquote><p>You're right, it is not in the block, but it doesn't have to be.</p></blockquote><p>Yes, but I would vote to have it there, as an explicit Interface ID is used in several other block, so why not here?</p></div><div id="comment-24995-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:04)</span> Kurt Knochner ♦</div></div><span id="24998"></span><div id="comment-24998" class="comment"><div id="post-24998-score" class="comment-score"></div><div class="comment-text"><p>It is necessary in other blocks to reference the interface. In the Interface Description Block it would say "0" for the first block, "1" for the second, and so on. Reading the blocks I can do that in code, incrementing the ID for each block I read, so having it in the block is kind of redundant information.</p><p>There is a "reserved" 16 bit block left in the IDB, so unless it is reserved with something else in mind we could use it for an index of up to 65535 interfaces.</p></div><div id="comment-24998-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:13)</span> Jasper ♦♦</div></div><span id="25008"></span><div id="comment-25008" class="comment"><div id="post-25008-score" class="comment-score"></div><div class="comment-text"><blockquote><p>incrementing the ID for each block I read, so <strong>having it in the block is kind of redundant information</strong>.</p></blockquote><p>yes that's true, but it requires an (kind of 'out of band') agreement how to handle/create the Interface ID, which needs to be part of the format/structure definition. Nothing wrong with that approach, but also kind of inconsistent in regards of the ID usage in the rest of the specs, especially as you don't loose much space if you add the ID into the block.</p></div><div id="comment-25008-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:41)</span> Kurt Knochner ♦</div></div><span id="25017"></span><div id="comment-25017" class="comment"><div id="post-25017-score" class="comment-score"></div><div class="comment-text"><p>well, there is an agreement like that, it's just not as specific as it should be. I'll consider using the free 16 bits for the ID, unless others have a veto. Waiting on Guy for his 2 cents ;-)</p></div><div id="comment-25017-info" class="comment-info"><span class="comment-age">(20 Sep '13, 04:53)</span> Jasper ♦♦</div></div><span id="25060"></span><div id="comment-25060" class="comment"><div id="post-25060-score" class="comment-score"></div><div class="comment-text"><p>Note that, given that pcap-ng files without an interface ID in the IDB already exist, no code can depend on there being an interface ID in the IDB, unless you change the minor version of pcap-ng and have some code (code that requires an interface ID in the IDB) incapable of reading the current version of pcap-ng, which strikes me as not an ideal situation.</p><p>Presumably the idea is that this would mean that, when writing pcap-ng 1.1 files, you wouldn't have to "keep the interfaces in the same order, or, if reordering them, renumber the interface IDs in all frames headers accordingly", but you'd still, when reading pcap-ng 1.0 files, have to assign the interface IDs based on the ordinal numbers of the IDBs. However, unless you choose not to support <em>writing</em> pcap-ng 1.0 files, you'd still have to have the code to keep the interfaces in the same order or renumber them.</p><p>The "out-of-band agreement how to handle the interface ID" is already in the pcap-ng spec; it's the quoted section of the spec in the answer.</p></div><div id="comment-25060-info" class="comment-info"><span class="comment-age">(20 Sep '13, 18:04)</span> Guy Harris ♦♦</div></div></div><div id="comment-tools-24987" class="comment-tools"></div><div class="clear"></div><div id="comment-24987-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

