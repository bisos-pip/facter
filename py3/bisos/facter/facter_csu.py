# -*- coding: utf-8 -*-
"""\
* *[Summary]* :: A /library/ Beginning point for development of new ICM oriented libraries.
"""

import typing

icmInfo: typing.Dict[str, typing.Any] = { 'moduleDescription': ["""
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Description:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Xref]          :: *[Related/Xrefs:]*  <<Xref-Here->>  -- External Documents  [[elisp:(org-cycle)][| ]]

**  [[elisp:(org-cycle)][| ]]   Model and Terminology                                      :Overview:
*** concept             -- Desctiption of concept
**      [End-Of-Description]
"""], }

icmInfo['moduleUsage'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Usage:* | ]]

**      How-Tos:
**      [End-Of-Usage]
"""

icmInfo['moduleStatus'] = """
*       [[elisp:(org-show-subtree)][|=]]  [[elisp:(org-cycle)][| *Status:* | ]]
**  [[elisp:(org-cycle)][| ]]  [Info]          :: *[Current-Info:]* Status/Maintenance -- General TODO List [[elisp:(org-cycle)][| ]]
** TODO [[elisp:(org-cycle)][| ]]  Current     :: For now it is an ICM. Turn it into ICM-Lib. [[elisp:(org-cycle)][| ]]
**      [End-Of-Status]
"""

"""
*  [[elisp:(org-cycle)][| *ICM-INFO:* |]] :: Author, Copyleft and Version Information
"""
####+BEGIN: bx:icm:py:name :style "fileName"
icmInfo['moduleName'] = "facterIcm"
####+END:

####+BEGIN: bx:icm:py:version-timestamp :style "date"
icmInfo['version'] = "202110193530"
####+END:

####+BEGIN: bx:icm:py:status :status "Production"
icmInfo['status']  = "Production"
####+END:

icmInfo['credits'] = ""

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/update/sw/icm/py/icmInfo-mbNedaGplByStar.py"
icmInfo['authors'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['copyright'] = "Copyright 2017, [[http://www.neda.com][Neda Communications, Inc.]]"
icmInfo['licenses'] = "[[https://www.gnu.org/licenses/agpl-3.0.en.html][Affero GPL]]", "Libre-Halaal Services License", "Neda Commercial License"
icmInfo['maintainers'] = "[[http://mohsen.1.banan.byname.net][Mohsen Banan]]"
icmInfo['contacts'] = "[[http://mohsen.1.banan.byname.net/contact]]"
icmInfo['partOf'] = "[[http://www.by-star.net][Libre-Halaal ByStar Digital Ecosystem]]"
####+END:

icmInfo['panel'] = "{}-Panel.org".format(icmInfo['moduleName'])
icmInfo['groupingType'] = "IcmGroupingType-pkged"
icmInfo['cmndParts'] = "IcmCmndParts[common] IcmCmndParts[param]"


####+BEGIN: bx:icm:python:top-of-file :partof "bystar" :copyleft "halaal+minimal"
"""
*  This file:/bisos/git/auth/bxRepos/bisos-pip/basics/py3/bisos/basics/facterIcm.py :: [[elisp:(org-cycle)][| ]]
 is part of The Libre-Halaal ByStar Digital Ecosystem. http://www.by-star.net
 *CopyLeft*  This Software is a Libre-Halaal Poly-Existential. See http://www.freeprotocols.org
 A Python Interactively Command Module (PyICM).
 Best Developed With COMEEGA-Emacs And Best Used With Blee-ICM-Players.
 *WARNING*: All edits wityhin Dynamic Blocks may be lost.
"""
####+END:

####+BEGIN: bx:icm:python:topControls :partof "bystar" :copyleft "halaal+minimal"
"""
*  [[elisp:(org-cycle)][|/Controls/| ]] :: [[elisp:(org-show-subtree)][|=]]  [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(delete-other-windows)][(1)]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]
"""
####+END:
####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/pyWorkBench.org"
"""
*  /Python Workbench/ ::  [[elisp:(org-cycle)][| ]]  [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
"""
####+END:

####+BEGIN: bx:icm:python:icmItem :itemType "=Imports=" :itemTitle "*IMPORTS*"
"""
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Imports=  :: *IMPORTS*  [[elisp:(org-cycle)][| ]]
"""
####+END:


import os
import collections
import pathlib
import invoke

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs, parsGetAsDictValue
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

from bisos.facter import facter

G = cs.globalContext.get()

####+BEGIN: b:py3:cs:orgItem/section :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *CSU-Lib Executions* -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

svcName = "svcFacter"
# roSiteRegistrarSapPath = cs.ro.SapBase_FPs.svcNameToRoSapPath(svcName, rosmu="svcInvSiteRegBox.cs")  # static method

cs.invOutcomeReportControl(cmnd=True, ro=True)


####+BEGIN: bx:dblock:python:section :title "ICM Commands"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *ICM Commands*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "examples_basic" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_basic/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_basic(
####+END:
        sectionTitle: typing.AnyStr = "",
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    if sectionTitle == "default":
        cs.examples.menuChapter('=facter BASIC Examples=')

    cmndName = "factName" ; cps=cpsInit() ;
    cmndArgs = "networking.interfaces.lo.bindings[0].address" ; menuItem(verbosity='none')

    cmndName = "facter_example" ; cps=cpsInit() ; cmndArgs = "" ; menuItem(verbosity='none')


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /examples_csu/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
    sectionTitle: typing.AnyStr = "",
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ]
    #+end_org """

    def cpsInit(): return collections.OrderedDict()
    def menuItem(verbosity): cs.examples.cmndInsert(cmndName, cps, cmndArgs, verbosity=verbosity) # 'little' or 'none'
    def execLineEx(cmndStr): cs.examples.execInsert(execLine=cmndStr)

    if sectionTitle == "default":
        cs.examples.menuChapter('=facter CS Examples=')

    cmndName = "factName" ; cmndArgs = "networking" ;
    cps=cpsInit() ;
    menuItem(verbosity='little')
    menuItem(verbosity='full')

    cmndName = "factName" ; cps=cpsInit() ;

    cmndArgs = "networking.primary" ; menuItem(verbosity='none')
    cmndArgs = "networking.interfaces.lo.bindings" ; menuItem(verbosity='none')
    cmndArgs = "networking.interfaces.lo.bindings[0].address" ; menuItem(verbosity='none')

    cs.examples.menuChapter('=facter Examples=')

    execLineEx("facter networking")
    execLineEx("facter networking.primary")
    execLineEx("facter networking.interfaces.lo.bindings")
    execLineEx("facter networking.interfaces.lo.bindings[0].address  # Fails, you can't do that")

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "facter_examples" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<facter_examples>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class facter_examples(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        examples_csu(sectionTitle="default")

        return(cmndOutcome)

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "factName" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<factName>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class factName(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Returns factValue for specified factName.
        #+end_org """)

        factName = self.cmndArgsGet("0", cmndArgsSpecDict, argsList)

        factValue = facter.get(factName)

        # print(factValue)

        return cmndOutcome.set(opResults=factValue,)


####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()

        cmndArgsSpecDict.argsDictAdd(
            argPosition="0",
            argName="factName",
            argDefault='',
            argChoices=[],
            argDescription="One Argument , any string for a factName"
        )

        return cmndArgsSpecDict


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Invoke Service Commands At Site Registrar" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Invoke Service Commands At Site Registrar_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:func/typing :funcName "roPerf_examples_csu" :comment "~CSU Specification~" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /roPerf_examples_csu/  ~CSU Specification~ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def roPerf_examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* |]] Examples of Service Access Instance Commands.
    #+end_org """

    cmndOutcome = b.op.Outcome()

    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter

    myName = cs.G.icmMyName()

    if myName == 'svcPerfSiteRegistrars.cs':
        svcName = 'svcSiteRegistrars'
        perfName = 'svcSiteRegistrars'
    elif myName == 'svcSiteRegistrars.cs':
        svcName = 'svcSiteRegistrars'
        perfName = 'svcSiteRegistrars'
    elif myName == 'svcSiteRegBox.cs':
        svcName = 'svcSiteRegBox'
        perfName = 'svcSiteRegBox'
    elif myName == 'svcSiteRegContainer.cs':
        svcName = 'svcSiteRegContainer'
        perfName = 'svcSiteRegContainer'
    elif myName == 'roPerf-facter.cs':
        svcName = 'svcFacter'
        perfName = 'me'
    else:
        svcName = 'MissingSvcName'
        perfName = 'MissingPerfName'

    if sectionTitle == 'default': cs.examples.menuChapter('*Remote Operations -- Performer SAP Create and Manage*')

    cmnd('perf_sapCreate', pars=od([('svcName', svcName), ('perfName', perfName)]))

    print(f"""csRo-manage.cs --svcName={svcName} --rosmu={myName}  -i ro_fps list""")

    cmnd('csPerformer', pars=od([('svcName', svcName)]), comment="&  #  in background Start rpyc CS Service" )

    # print(f"""svcSiteRegBox.cs --perfName="siteRegistrar" -i csPerformer  & # in background Start rpyc CS Service""")



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "perf_sapCreate" :ro "noCli" :comment "" :parsMand "svcName perfName" :parsOpt "rosmuControl" :argsMin 0 :argsMax 0
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<perf_sapCreate>>  =verify= parsMand=svcName perfName parsOpt=rosmuControl ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class perf_sapCreate(cs.Cmnd):
    cmndParamsMandatory = [ 'svcName', 'perfName', ]
    cmndParamsOptional = [ 'rosmuControl', ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             svcName: typing.Optional[str]=None,  # Cs Mandatory Param
             perfName: typing.Optional[str]=None,  # Cs Mandatory Param
             rosmuControl: typing.Optional[str]=None,  # Cs Optional Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'svcName': svcName, 'perfName': perfName, 'rosmuControl': rosmuControl, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        svcName = csParam.mappedValue('svcName', svcName)
        perfName = csParam.mappedValue('perfName', perfName)
        rosmuControl = csParam.mappedValue('rosmuControl', rosmuControl)
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Invoked both by invoker and performer. Creates path for ro_sap and updates FPs
        """
        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  svcSiteRegistrars.cs --rosmu svcSiteRegistrars.cs -i reg_sapCreateBox
#+end_src
#+RESULTS:
#+begin_example

FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfIpAddr/value value=localhost
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfPortNu/value value=22222003
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/accessControl/value value=placeholder
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfName/value value=siteRegistrar
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfModel/value value=rpyc
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/rosmu/value value=svcSiteRegistrars.cs
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/rosmuSel/value value=default
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/rosmuControl/value value=bisos
/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default
#+end_example

#+begin_src sh :results output :session shared
  svcSiteRegistrars.cs -i reg_sapCreateBox
#+end_src
#+RESULTS:
:
: bash: svcSiteRegistrars.cs: command not found
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome

        perfModel = "rpyc"
        rosmu = cs.G.icmMyName()

        perfName = perfName
        rosmuSel = "default"
        rosmuControl = 'bisos'
        perfIpAddr = "localhost"

        if (perfPortList := bannaPortNu.bannaPortNuOf().pyWCmnd(cmndOutcome,
                argsList=[svcName]
        ).results) == None : return failed(cmndOutcome)

        perfPortNu = perfPortList[0]

        sapBaseFps = b.pattern.sameInstance(cs.ro.SapBase_FPs, rosmu=rosmu, svcName=svcName, perfName=perfName, perfModel=perfModel, rosmuSel=rosmuSel)

        sapBaseFps.fps_setParam('perfIpAddr', perfIpAddr)
        sapBaseFps.fps_setParam('perfPortNu', perfPortNu)
        sapBaseFps.fps_setParam('accessControl', "placeholder")
        sapBaseFps.fps_setParam('perfName', perfName)
        sapBaseFps.fps_setParam('perfModel', perfModel)
        sapBaseFps.fps_setParam('rosmu', rosmu)
        sapBaseFps.fps_setParam('rosmuSel', rosmuSel)
        sapBaseFps.fps_setParam('rosmuControl', rosmuControl)

        sapPath = sapBaseFps.basePath_obtain()

        return cmndOutcome.set(opResults=sapPath,)


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Invoke Service Commands At Site Registrar" :anchor ""  :extraInfo "Command Services Section"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Invoke Service Commands At Site Registrar_: |]]  Command Services Section  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:func/typing :funcName "roInv_examples_csu" :comment "~CSU Specification~" :funcType "eType" :retType "" :deco "default" :argsList ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /roInv_examples_csu/  ~CSU Specification~ deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def roInv_examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr* |]] Examples of Service Access Instance Commands.
    #+end_org """

    cmndOutcome = b.op.Outcome()

    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter

    perfIpAddr = 'localhost'
    perfName = 'HSS-1012'

    unitsPars = collections.OrderedDict([])

    if sectionTitle == 'default': cs.examples.menuChapter('*Remote Operations --Invoker Management*')

    cmnd('invSapCreate', pars=od([('perfName', perfName), ('perfIpAddr', perfIpAddr)]))
    print(f"""csRo-manage.cs --svcName="svcSiteRegBox" --rosmu="svcSiteRegBox.cs"  -i ro_fps list""")

    if sectionTitle == 'default': cs.examples.menuChapter('*Registrar Svc Commands -- perfName=siteRegistrar*')

    # cmnd('reg_box_find', pars=unitsPars, args=findArgs,)
    cmnd('reg_box_list', pars=unitsPars)



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "invSapCreate" :ro "noCli" :comment "" :parsMand "perfName perfIpAddr" :parsOpt "" :argsMin 0 :argsMax 0
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<invSapCreate>>  =verify= parsMand=perfName perfIpAddr ro=noCli   [[elisp:(org-cycle)][| ]]
#+end_org """
class invSapCreate(cs.Cmnd):
    cmndParamsMandatory = [ 'perfName', 'perfIpAddr', ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo() # NO RO From CLI

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             perfName: typing.Optional[str]=None,  # Cs Mandatory Param
             perfIpAddr: typing.Optional[str]=None,  # Cs Mandatory Param
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {'perfName': perfName, 'perfIpAddr': perfIpAddr, }
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
        perfName = csParam.mappedValue('perfName', perfName)
        perfIpAddr = csParam.mappedValue('perfIpAddr', perfIpAddr)
####+END:
        """\
***** [[elisp:(org-cycle)][| *CmndDesc:* | ]] Invoked both by invoker and performer. Creates path for ro_sap and updates FPs
        """
        self.captureRunStr(""" #+begin_org
#+begin_src sh :results output :session shared
  svcInvSiteRegBox.cs --rosmu svcSiteRegistrars.cs -i reg_sapCreateBox
#+end_src
#+RESULTS:
#+begin_example

FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfIpAddr/value value=localhost
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfPortNu/value value=22222003
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/accessControl/value value=placeholder
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfName/value value=siteRegistrar
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/perfModel/value value=rpyc
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/rosmu/value value=svcSiteRegistrars.cs
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/rosmuSel/value value=default
FileParam.writeTo path=/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default/rosmuControl/value value=bisos
/bisos/var/cs/ro/sap/svcSiteRegistrars.cs/siteRegistrar/rpyc/default
#+end_example

#+begin_src sh :results output :session shared
  svcSiteRegistrars.cs -i reg_sapCreateBox
#+end_src
#+RESULTS:
:
: bash: svcSiteRegistrars.cs: command not found
        #+end_org """)
        if self.justCaptureP(): return cmndOutcome

        perfModel = "rpyc"
        rosmu = cs.G.icmMyName()

        rosmuSel = 'default'  #  A file path to
        rosmuControl = 'bisos'

        if (perfPortList := bannaPortNu.bannaPortNuOf().pyWCmnd(cmndOutcome,
                argsList=[svcName]
        ).results) == None : return failed(cmndOutcome)

        perfPortNu = perfPortList[0]

        sapBaseFps = b.pattern.sameInstance(cs.ro.SapBase_FPs, rosmu=rosmu, svcName=svcName, perfName=perfName, perfModel=perfModel, rosmuSel=rosmuSel)

        sapBaseFps.fps_setParam('svcName', svcName)
        sapBaseFps.fps_setParam('perfIpAddr', perfIpAddr)
        sapBaseFps.fps_setParam('perfPortNu', perfPortNu)
        sapBaseFps.fps_setParam('accessControl', "placeholder")
        sapBaseFps.fps_setParam('perfName', perfName)
        sapBaseFps.fps_setParam('perfModel', perfModel)
        sapBaseFps.fps_setParam('rosmu', rosmu)
        sapBaseFps.fps_setParam('rosmuSel', rosmuSel)
        sapBaseFps.fps_setParam('rosmuControl', rosmuControl)

        sapPath = sapBaseFps.basePath_obtain()

        return cmndOutcome.set(opResults=sapPath,)


####+BEGIN: bx:icm:python:section :title "End Of Editable Text"
"""
*  [[elisp:(beginning-of-buffer)][Top]] ############## [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] [[elisp:(delete-other-windows)][(1)]]    *End Of Editable Text*  [[elisp:(org-cycle)][| ]]  [[elisp:(org-show-subtree)][|=]]
"""
####+END:

####+BEGIN: bx:dblock:global:file-insert-cond :cond "./blee.el" :file "/bisos/apps/defaults/software/plusOrg/dblock/inserts/endOfFileControls.org"
#+STARTUP: showall
####+END:
