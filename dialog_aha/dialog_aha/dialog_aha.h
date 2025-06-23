
// dialog_aha.h : main header file for the PROJECT_NAME application
//

#pragma once

#ifndef __AFXWIN_H__
	#error "include 'pch.h' before including this file for PCH"
#endif

#include "resource.h"		// main symbols


// CdialogahaApp:
// See dialog_aha.cpp for the implementation of this class
//

class CdialogahaApp : public CWinApp
{
public:
	CdialogahaApp();

// Overrides
public:
	virtual BOOL InitInstance();

// Implementation

	DECLARE_MESSAGE_MAP()
};

extern CdialogahaApp theApp;
